from construct import *

from .common import String, Bool, Message
from .enums import DisconnectReason, SendOption

# DISCONNECT
from .network_messages import Message_Client, Message_Server

DisconnectReasonInfo = Struct(
            "DisconnectReason" / DisconnectReason,
            "DisconnectMessage" / If(this.DisconnectReason == DisconnectReason.Custom, String)
)

DisconnectBody_Client = Terminated
DisconnectBody_Server = Struct(
    "HasDisconnectReasonInfo" / Bool,
    "ForcibleDisconnectMessage" / If(this.HasDisconnectReasonInfo, Message(Const(0, Byte), DisconnectReasonInfo))
)


# HELLO
HelloBody_Client = Struct(
    "HazelVersion" / Const(0, Byte),
    "ClientVersion_Maybe" / Int32ul,
    "Name" / String,
)
HelloBody_Server = Error # The Server should NEVER send a Hello



# TOP-LEVEL DISPATCHER LOGIC
def Packet(unreliable_subcon, reliable_subcon, disconnect_subcon, hello_subcon=None):
    hello_subcon = GreedyBytes if hello_subcon is None else hello_subcon
    return Struct(
        "SendOption" / SendOption,
        "Seq" / Switch(this.SendOption, cases={
            SendOption.Reliable: Int16ub,
            SendOption.Ping: Int16ub,
            SendOption.Acknowledgement: Int16ub,
            }, default=Pass),
        "payload" / Switch(
            keyfunc=this.SendOption, cases={
                SendOption.Unreliable: unreliable_subcon,
                SendOption.Reliable: reliable_subcon,
                SendOption.Ping: Int16ub,
                SendOption.Acknowledgement: Const(0xff, Byte),
                SendOption.Hello: hello_subcon,
                SendOption.Disconnect: disconnect_subcon,
            },
            default=Error,
        )
    )

Packet_Client = Packet(
    unreliable_subcon=GreedyRange(Message_Client),
    reliable_subcon=GreedyRange(Message_Client),
    disconnect_subcon=DisconnectBody_Client,
    hello_subcon=HelloBody_Client
) + Terminated

Packet_Server = Packet(
    unreliable_subcon=GreedyRange(Message_Server),
    reliable_subcon=GreedyRange(Message_Server),
    disconnect_subcon=DisconnectBody_Server,
    hello_subcon=HelloBody_Server
) + Terminated