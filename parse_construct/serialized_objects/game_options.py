from construct import *

from parse_construct.common import Bool
from parse_construct.enums import GameLanguage

GameOptions = Struct(
    "SomeVersionOrSizeFlag" / Byte,
    "ALGKPIECFPC" / Byte,
    "SystemLanguage" / GameLanguage,
    "BFOCEACJOPK" / Byte,
    "PlayerSpeedMultiplier" / Float32l,
    "LNKCMDOCNBI" / Float32l,
    "NFAOBDJKOPH" / Float32l,
    "HNEKLLKCJOJ" / Float32l,
    "LNNGPNHGGDN" / Byte,
    "FFJKPGELKGD" / Byte,
    "OJLANPDBDGG" / Byte,
    "JOLOOHKAIAB" / Int32sl,
    "MAONBFOOEPK" / Byte,
    "MCHMMCDKECO" / Byte,
    "IECOKEIAEEE" / Int32sl,
    "MMJKMHKEAPI" / Int32sl,
    "MEIOIAOIBOH" / Bool,
    If(this.SomeVersionOrSizeFlag >= 2, "OEBNJBBLHBD" / Byte),
    If(this.SomeVersionOrSizeFlag >= 3, "BELGPJKBKGA" / Bool + "KPFLIHLKEBI" / Bool)
)