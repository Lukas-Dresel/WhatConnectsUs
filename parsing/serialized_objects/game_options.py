from construct import *

from ..common import Bool
from ..enums import GameLanguage, KillDistance, LevelId

GameOptions = Struct(
    "Version" / Byte,
    "NumPlayers" / Byte,
    "SystemLanguage" / GameLanguage,
    "Level" / LevelId,
    "PlayerSpeedMultiplier" / Float32l,
    "CrewmateVisionMultiplier" / Float32l,
    "ImpostorVisionMultiplier" / Float32l,
    "KillCooldown" / Float32l,
    "NumCommonTasks" / Byte,
    "NumLongTasks" / Byte,
    "NumShortTasks" / Byte,
    "NumEmergencyMeetings" / Int32sl,
    "NumImpostors" / Byte,
    "KillDistance" / KillDistance,
    "DiscussionTime" / Int32sl,
    "VotingTime" / Int32sl,
    "UseRecommendedSettings" / Bool,
    "EmergencyCooldown" / If(this.Version >= 2, Byte),
    "ConfirmEjects" / If(this.Version >= 3, Bool),
    "VisualTasks" / If(this.Version >= 3, Bool),
)