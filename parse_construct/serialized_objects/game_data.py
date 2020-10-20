from construct import *

from .player_data import PlayerData

GameData = Struct(
    "NumPlayers" / VarInt,
    "Players" / Struct(
        "PlayerId" / Byte,
        "data" / PlayerData,
    )[this.NumPlayers]
)