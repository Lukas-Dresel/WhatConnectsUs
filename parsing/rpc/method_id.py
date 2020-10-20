from construct import Enum, Byte

MethodId = Enum(Byte,
                # PlayerControl
                RpcPlayAnimation    =   0x00,
                RpcCompleteTask     =   0x01,
                RpcSyncSettings     =   0x02,
                RpcSetInfected      =   0x03,
                CmdCheckName        =   0x05,
                ResponseCheckName   =   0x06,
                CmdCheckColor       =   0x07,
                ResponseCheckColor  =   0x08,
                SetHat              =   0x09,
                SetSkin             =   0x0A,
                CmdReportDead       =   0x0b,
                RpcMurderPlayer     =   0x0c,
                RpcSendChat         =   0x0d,
                RpcStartMeeting     =   0x0e,
                RpcSetScanner       =   0x0f,
                RpcSendChatNote     =   0x10,
                SetPet              =   0x11,
                SetStartCounter     =   0x12,

                # PlayerPhysics
                EnterVent           =   0x13,
                ExitVent            =   0x14,

                # CustomNetworkTransform
                SnapTo              =   0x15,

                # MeetingHud
                CloseMeetingHud     =   0x16,
                VotingComplete      =   0x17,
                CastVote            =   0x18,
                ClearVote           =   0x19,

                # GameData
                GameDate_UpdatePlayerTaskCompletion     =   0x1d,
                UpdateGameData      =   0x1e,
                )