from construct import *

from .method_id import MethodId
from ..common import PlayerId, BytesAndSize, Bool

ALL_RPCCalls_MeetingHud = {
    MethodId.CloseMeetingHud: Terminated,
    MethodId.VotingComplete: Struct(
        "StateSomehow" / BytesAndSize,
        "PlayerIdOfPlayerVotedOff_Or_MinusOne" / PlayerId,
        "WasTie" / Bool,
    ),
    MethodId.CastVote: Struct("VotingPlayerId" / PlayerId, "VotedForPlayerId" / PlayerId),
    MethodId.ClearVote: Terminated,
}