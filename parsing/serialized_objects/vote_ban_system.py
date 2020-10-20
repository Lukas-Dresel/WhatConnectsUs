from construct import *

VoteBanSystem_Record = Struct(
    "unk_uint_1" / Int32ul,
    "args" / Int32ul[4],
)
VoteBanSystem = Struct(
    "NumVotes" / Byte,
    "vote_records_maybe" / VoteBanSystem_Record[this.NumVotes],
)