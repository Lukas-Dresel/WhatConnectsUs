import argparse

from scapy.all import *
import hexdump

from parse_construct.enums import SendOption
from parse_construct.network_packets import Packet_Server, Packet_Client


def pkt_callback(pkt):
    ip = pkt[IP] if IP in pkt else None
    udp = pkt[UDP] if UDP in pkt else None
    if ip is None or udp is None:
        return
    
    direction = (udp.sport, udp.dport)
    if ARGS.port not in direction:
        return
    data = bytes(udp.payload)
    if data[0] in {SendOption.Ping.intvalue, SendOption.Acknowledgement.intvalue}:
        return

    print(repr(data))
    description = '{:05d}->{:05d} {:2d}: {}'.format(udp.sport, udp.dport, data[0], hexdump.dump(data[1:]))
    print(description)
    Packet = Packet_Client if direction[1] == ARGS.port else Packet_Server
    parsed_pkt = Packet.parse(data)
    print(parsed_pkt)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=22023)
    parser.add_argument('--source', type=str, default='live')
    ARGS = parser.parse_args()

    print("Listening ...")
    if ARGS.source == 'live':
        sniff(prn=pkt_callback, filter=f"udp port {ARGS.port}", store=0)
    else:
        sniff(offline=ARGS.source, prn=pkt_callback)
