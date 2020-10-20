import ipdb
from construct import *

from .custom_network_transform import ALL_RPCCalls_CustomNetworkTransform
from .method_id import MethodId

from .player_control import ALL_RPCCalls_PlayerControl
from .meeting_hud import ALL_RPCCalls_MeetingHud
from .game_data import ALL_RPCCalls_GameData
from .player_physics import ALL_RPCCalls_PlayerPhysics
from ..common import NetId

ALL_RPCArguments = dict(
    **ALL_RPCCalls_PlayerControl,
    **ALL_RPCCalls_PlayerPhysics,
    **ALL_RPCCalls_CustomNetworkTransform,
    **ALL_RPCCalls_MeetingHud,
    **ALL_RPCCalls_GameData
)
RPC = Struct(
    "NetId" / NetId,
    "MethodId" / MethodId,
    "Arguments" / Switch(this.MethodId, cases=ALL_RPCArguments, default=LazyBound(lambda: ipdb.set_trace() or Error)),
)


