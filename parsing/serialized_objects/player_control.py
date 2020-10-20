from construct import *

PlayerControl = Struct(
    "PHNNGIGNMEG" / Byte,
    "PlayerId" / Byte,
)