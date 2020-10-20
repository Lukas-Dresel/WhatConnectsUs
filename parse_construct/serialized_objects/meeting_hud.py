from construct import *

from parse_construct.common import DirtyBits


class VotedForAdapter(Adapter):
    def _decode(self, obj, context, path):
        return obj - 1
    def _encode(self, obj, context, path):
        return obj + 1


def count_ones(dirtybits):
    return sum(1 if c == '1' else 0 for c in bin(dirtybits)[2:])


PlayerVoteArea = BitStruct(
    "IsDead" / Flag,
    "DidVote" / Flag,
    "DidReport" / Flag,
    Padding(1),
    "VotedFor" / VotedForAdapter(Nibble),
)

MeetingHud_Full = Struct(
    "VoteAreas" / GreedyRange(PlayerVoteArea)
)

MeetingHud_Partial = Struct(
    "DirtyBits" / DirtyBits,
    "VoteAreas" / PlayerVoteArea[lambda ctx: count_ones(ctx.DirtyBits)],
)