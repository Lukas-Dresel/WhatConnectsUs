from construct import *

from .common import Message, GameId, PlayerId, NetId, debug_field, String, PackedUInt, PackedInt, \
    ClientId, Bool
from .enums import Levels, MessageTypes, UpdateTypes, SpawnFlags, SpawnId, DisconnectReason
from .rpc import RPC
from .serialized_objects import PlayerControl, CustomNetworkTransform, GameData, VoteBanSystem, MeetingHud_Full
from .serialized_objects.game_options import GameOptions


class SerializedComponentAdapter(Adapter):
    def _decode(self, obj, context, path):
        return Container(NetId=obj.NetId, Serialized=obj.Serialized.payload)

    def _encode(self, obj, context, path):
        return {'NetId': obj[0], 'Serialized': {'tag': 1, 'payload': obj[1]}}


def SerializedComponent(payload_subcon):
    return SerializedComponentAdapter(Struct(
        "NetId" / NetId,
        "Serialized" / Message(Const(1, Byte), payload_subcon)
    ))


UpdateContent = Message(UpdateTypes, Switch(this.tag, cases={
    UpdateTypes.FixedUpdate: Struct(
        "NetId" / NetId,
        "Update" / GreedyBytes
    ),
    UpdateTypes.RPC: RPC,
    UpdateTypes.Spawn: Struct(
        "SpawnId" / SpawnId,
        "OwnerId" / PackedInt,
        "SpawnFlags" / SpawnFlags,
        "NumComponents" / Rebuild(VarInt, len_(this.Components)),
        "Components" / Switch(this.SpawnId, cases={
            SpawnId.ShipStatus: Struct(
                "ShipStatus" / SerializedComponent(debug_field(GreedyBytes)),
                # TODO: needs to eventually be ShipStatus_Full
            ),
            SpawnId.MeetingHub: Struct(
                "MeetingHud" / SerializedComponent(debug_field(MeetingHud_Full)),
            ),
            SpawnId.Lobby: Struct(
                "LobbyBehaviour" / SerializedComponent(Pass),
            ),
            SpawnId.GameData: Struct(
                "GameData" / SerializedComponent(GameData),
                "VoteBanSystem" / debug_field(SerializedComponent(VoteBanSystem)),
            ),
            SpawnId.Player: Struct(
                "PlayerControl" / SerializedComponent(PlayerControl),
                "PlayerPhysics" / SerializedComponent(Pass),
                "CustomNetworkTransform" / SerializedComponent(CustomNetworkTransform),
            ),
        },
                              default=Error
                              )
    ),
    UpdateTypes.Despawn: Struct(
        "NetId" / NetId,
    ),
    UpdateTypes.ChangeScene: Struct(
        "ClientId" / VarInt,
        "SceneName" / Const(u'OnlineGame', String),
    )
},
                                            default=Error
                                            ))


class IpAddressAdapter(Adapter):
    def _decode(self, obj, context, path):
        return ".".join(map(str, obj))

    def _encode(self, obj, context, path):
        return list(map(int, obj.split(".")))


MasterServerListEntry = Message(Byte, Struct(
    "ServerNameMaybe" / String,
    "IPAddress" / IpAddressAdapter(Byte[4]),
    "PortMaybe" / Int16ul,
    "UnknownInt32" / PackedUInt,
)
                                )
SharedMessages = {
    MessageTypes.StartGame: Struct(
        "GameId" / GameId
    ),
    MessageTypes.RemovePlayer: Struct(
        "GameId" / GameId,

    ),
    MessageTypes.BroadcastUpdate: Struct(
        "GameId" / GameId,
        "Messages" / GreedyRange(UpdateContent)
    ),
    MessageTypes.TargetUpdate: Struct(
        "GameId" / GameId,
        "TargetId" / VarInt,
        "body" / GreedyRange(UpdateContent)
    ),
    MessageTypes.InfoForJoinedGame: Struct(
        "GameId" / GameId,
        "ClientId" / ClientId,
        "HostId" / Int32ul,
        "OtherClients" / PrefixedArray(PackedUInt, PackedUInt),
    ),
    MessageTypes.EndGame: Struct(
        "GameId" / GameId,
        "Reason" / Byte,
        "ShowAd" / Bool,
    ),
    MessageTypes.ChangeGamePublic: Struct(
        "GameId" / GameId,
        "ShouldBePublic" / Byte,
        "unk_byte_1" / Byte,
    ),
    MessageTypes.KickPlayerMessage: Struct(
        "GameId" / GameId,
        "PlayerId" / PlayerId,
        "CanRejoin" / Byte,
    ),
    MessageTypes.OtherPlayerClientJoined: Struct(
        "GameId" / GameId,
        "ClientId" / ClientId,
    ),
    MessageTypes.RedirectToActualGameServer: Struct(
        "Address" / IpAddressAdapter(Byte[4]),
        "Port" / Int16ul,
    ),
    MessageTypes.MasterServerList: Struct(
        "Ignored" / Byte,
        "ServerList" / PrefixedArray(PackedUInt, MasterServerListEntry)
    )
}

JoinGame_ServerResponse = Select(
    # Option 1: DisconnectCode + DisconnectReason
    Struct(
        "IsError" / Computed(lambda ctx: True),
        "DisconnectCode" / DisconnectReason,
        "DisconnectMessage" / If(this.DisconnectCode == DisconnectReason.Custom, String)
    ),
    # Option 2: GameId
    Struct(
        "IsError" / Computed(lambda ctx: False),
        "GameId" / GameId,
        "TargetClientId" / Int32ul,
        "HostId" / Int32ul,
    )
)
MessageTypes_ClientOnly = {
    MessageTypes.HostGame: Struct(
        "GameOptions" / Prefixed(PackedInt, GameOptions)
    ),
    MessageTypes.JoinGame: Struct(
        "GameId" / GameId,
        "OwnedMaps" / Levels
    ),
}

Message_Client = Message(MessageTypes, Switch(
    this.tag,
    cases=dict(**MessageTypes_ClientOnly, **SharedMessages),
    default=Error
)
                         )

MessageTypes_ServerOnly = {
    MessageTypes.HostGame: Struct(
        "GameCode" / Int32ul,
    ),
    MessageTypes.JoinGame: JoinGame_ServerResponse
}
Message_Server = Message(MessageTypes, Switch(
    this.tag,
    cases=dict(**MessageTypes_ServerOnly, **SharedMessages),
    default=Error
)
                         )
