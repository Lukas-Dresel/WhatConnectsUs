import ipdb
from construct import *

class SignedVarInt32Adapter(Adapter):
    def _decode(self, obj, context, path):
        return obj if obj & (1<<31) == 0 else (1<<32) - obj

    def _encode(self, obj, context, path):
        return obj if obj > 0 else (1<<32) + obj

PackedUInt = VarInt
PackedInt = SignedVarInt32Adapter(VarInt)

String = Prefixed(PackedInt, GreedyString('utf8'))
BytesAndSize = Prefixed(PackedInt, GreedyBytes)


def debug_field(subcon):
    return LazyBound(lambda: ipdb.set_trace() or subcon)


Bool = Enum(Byte, false=0, true=1)
GameId = Hex(Int32ul)
NetId = PackedInt
PlayerId = VarInt
DirtyBits = PackedInt
ClientId = Int32ul

HatId = PackedInt
SkinId = PackedInt
PetId = PackedInt



def Message(tag_subcon, payload_subcon):
    return Struct(
    "len" / Rebuild(Int16ul, lambda this: this._subcons.payload.sizeof()),
    "tag" / tag_subcon,
    "payload" / FixedSized(this.len, payload_subcon),
)
