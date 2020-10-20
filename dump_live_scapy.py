import argparse

from scapy.all import *
import hexdump

from parsing.enums import SendOption
from parsing.network_packets import Packet_Server, Packet_Client

PORTS_OF_INTEREST = {22023 + i for i in range(0, 1000, 100)}
def pkt_callback(pkt):
    ip = pkt[IP] if IP in pkt else None
    udp = pkt[UDP] if UDP in pkt else None
    if ip is None or udp is None:
        return
    
    direction = (udp.sport, udp.dport)
    if udp.sport not in PORTS_OF_INTEREST and udp.dport not in PORTS_OF_INTEREST:
        return

    data = bytes(udp.payload)
    if data[0] in {SendOption.Ping.intvalue, SendOption.Acknowledgement.intvalue}:
        return

    print(repr(data))
    description = '{:05d}->{:05d} {:2d}: {}'.format(udp.sport, udp.dport, data[0], hexdump.dump(data[1:]))
    print(description)
    Packet = Packet_Client if direction[1] in PORTS_OF_INTEREST else Packet_Server
    parsed_pkt = Packet.parse(data)
    print(parsed_pkt)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('source', type=str, nargs='?', default='live')
    ARGS = parser.parse_args()

    print("Listening ...")
    if ARGS.source == 'live':
        filter = ' or '.join(f'udp port {port}' for port in sorted(PORTS_OF_INTEREST))
        print(filter)
        sniff(prn=pkt_callback, filter=filter, store=0)
    else:
        sniff(offline=ARGS.source, prn=pkt_callback)
