from construct import *

from ..common import debug_field, DirtyBits

ShipStatus_Partial = Struct(
    "DirtyBits" / DirtyBits,
    "NumSystems" / VarInt,
    "Systems" / debug_field(Byte[this.NumSystems]),
)

ShipStatus_Full = Struct(

)