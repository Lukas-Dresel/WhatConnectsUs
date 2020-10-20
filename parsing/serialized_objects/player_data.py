from construct import *

from ..common import String, HatId, PetId, SkinId, PackedInt
from ..enums import PlayerState, Color

TaskCompletion = Struct(
    "TaskIndex" / PackedInt,
    "Completed" / Byte,
)
PlayerData = Struct(
    "Name" / String,
    "ColorId" / Color,
    "HatId" / HatId,
    "PetId" / PetId,
    "SkinId" / SkinId,
    "PlayerStateFlags" / PlayerState,
    "NumTasks" / Byte,
    "Tasks" / TaskCompletion[this.NumTasks]
)