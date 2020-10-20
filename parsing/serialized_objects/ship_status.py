from construct import *

from parse_construct.common import debug_field, DirtyBits

ShipStatus_Partial = Struct(
    "DirtyBits" / DirtyBits,
    "NumSystems" / VarInt,
    "Systems" / debug_field(Byte[this.NumSystems]),
)

ShipStatus_Full = Struct(

)