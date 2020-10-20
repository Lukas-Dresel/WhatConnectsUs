from construct import *

from .method_id import MethodId
from ..common import PackedUInt
from ..serialized_objects.vector2 import NormalizedVector

ALL_RPCCalls_CustomNetworkTransform = {
    MethodId.SnapTo:             Struct("NewPosition" / NormalizedVector, "UpdateCount" / Int16ul),
}