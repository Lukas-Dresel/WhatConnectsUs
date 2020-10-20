from construct import *

from .method_id import MethodId
from ..common import Message, String, debug_field, PlayerId

#RPC_NotSureYet = RPCCall(Const(0x1D, MethodId), Struct("PlayerId" / Byte, Prefixed(VarInt, GreedyBytes)))
from ..serialized_objects.player_data import PlayerData

TaskCompletion = PrefixedArray(Byte, Byte)
ALL_RPCCalls_GameData = {
    MethodId.GameDate_UpdatePlayerTaskCompletion: Struct("PlayerId" / PlayerId, "Tasks" / debug_field(TaskCompletion)),
    MethodId.UpdateGameData: GreedyRange(Message(Byte, PlayerData))
}
