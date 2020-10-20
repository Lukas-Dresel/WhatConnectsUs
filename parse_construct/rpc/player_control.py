import ipdb
from construct import *

from .method_id import MethodId
from ..common import PlayerId, String, BytesAndSize, NetId, PackedInt
from ..serialized_objects.game_options import GameOptions

ALL_RPCCalls_PlayerControl = {
    MethodId.RpcPlayAnimation:      Struct("AnimationId" / Byte),
    MethodId.RpcCompleteTask:       Struct("TaskIndex" / PackedInt),
    MethodId.RpcSyncSettings:       Struct("GameOptions" / Prefixed(VarInt, GameOptions)),
    MethodId.RpcSetInfected:        Struct("Data" / BytesAndSize),
    MethodId.CmdCheckName:          Struct("Name" / String),
    MethodId.ResponseCheckName:     Struct("Name" / String),
    MethodId.CmdCheckColor:         Struct("ColorId" / Byte),
    MethodId.ResponseCheckColor:    Struct("ColorId" / Byte),
    MethodId.SetHat:                Struct("HatId" / PackedInt),
    MethodId.SetSkin:               Struct("SkinId" / PackedInt),
    MethodId.CmdReportDead:         Struct("PlayerId" / PlayerId),
    MethodId.RpcMurderPlayer:       Struct("NetId" / NetId),
    MethodId.RpcSendChat:           Struct("Message" / String),
    MethodId.RpcStartMeeting:       Struct("PlayerIdOrMinusOne" / Byte),
    MethodId.RpcSetScanner:         Struct("active_or_done_maybe" / Byte, "some_player_field" / Byte),
    MethodId.RpcSendChatNote:       Struct("SourcePlayerId" / PlayerId, "Notify" / Byte),
    MethodId.SetPet:                Struct("PetId" / PackedInt),
    MethodId.SetStartCounter:       Struct("SequenceNumber" / VarInt, "SecondsLeft  " / Byte),
}