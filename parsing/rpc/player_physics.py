from construct import *

from .method_id import MethodId
from ..common import PackedUInt


ALL_RPCCalls_PlayerPhysics = {
    MethodId.EnterVent:             Struct("VentIndex" / PackedUInt),
    MethodId.ExitVent:              Struct("VentIndex" / PackedUInt),
}