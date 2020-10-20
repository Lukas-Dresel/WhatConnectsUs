from construct import *
from .vector2 import NormalizedVector

CustomNetworkTransform = Struct(
    "UpdateCount" / Int16ul,
    "Position" / NormalizedVector,
    "Velocity" / NormalizedVector,
)
