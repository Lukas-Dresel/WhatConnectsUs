from construct import *

from .common import PackedInt
from .utils import FixedEnum

SendOption = Enum(Byte, Unreliable=0, Reliable=1, Hello=8, Disconnect=9, Acknowledgement=10, Fragment=11, Ping=12)

MessageTypes = Enum(Byte,
                    HostGame=0,
                    JoinGame=1,
                    StartGame=2,
                    RemoveGame=3,
                    RemovePlayer=4,
                    BroadcastUpdate=5,
                    TargetUpdate=6,
                    InfoForJoinedGame=7,
                    EndGame=8,
                    ChangeGamePublic=10,
                    KickPlayerMessage=11,
                    OtherPlayerClientJoined=12,
                    RedirectToActualGameServer=13,
                    MasterServerList=14,
                    RequestGameList=16,
                    )

# from DKJKABPBLDL__Enum
# Unfortunately we HAVE to have this a `FixedEnum` because invalid values here have to be interpreted as GameIds instead
DisconnectReason = FixedEnum(Byte,
                             ExitGame=0,
                             GameFull=1,
                             GameStarted=2,
                             GameNotFound=3,
                             LEGACY_Custom=4,
                             IncorrectVersion=5,
                             Banned=6,
                             Kicked=7,
                             Custom=8,
                             InvalidName=9,
                             Hacking=10,
                             Destroy=0x10,  # I KNOW THIS LOOKS WEIRD, but it's correct. Trust me
                             Error=0x11,
                             IncorrectGame=0x12,
                             ServerRequest=0x13,
                             ServerFull=0x14,
                             FocusLostBackground=0xCF,
                             IntentionalLeaving=0xD0,
                             FocusLost=0xD1,
                             NewConnection=0xD2,
                             )

UpdateTypes = Enum(Byte,
                   FixedUpdate=1,
                   RPC=2,
                   Spawn=4,
                   Despawn=5,
                   ChangeScene=6,
                   )

PlayerState = FlagsEnum(Byte, Infected=2)
GameLanguage = FlagsEnum(Int32ul, All=0, Other=1, Spanish=2, Korean=4, Russian=8, Portuguese=0x10, Arabic=0x20,
                         Filipino=0x40, Polish=0x80, English=0x100)
Color = Enum(Byte, Red=0, Blue=1, Green=2, Pink=3, Orange=4, Yellow=5, Black=6, White=7, Purple=8, Brown=9, Cyan=10,
             Lime=11, Fortegreen=12, Tan=13)
Levels = FlagsEnum(PackedInt, Skeld=1, MiraHQ=2, Polus=4)

Systems = Enum(Byte, Hallway=0, Storage=1, Cafeteria=2, Reactor=3, UpperEngine=4, Nav=5, Admin=6, Electrical=7,
               LifeSupport_O2=8, Shields=9, MedBay=10, Security=11, Weapons=12, LowerEngine=13, Comms=14, ShipTasks=15,
               Doors=16, Sabotage=17, Decontamination=18, Launchpad=19, LockerRoom=20, Laboratory=21, Balcony=22,
               Office=23, Greenhouse=24, Dropship=25, Decontamination2=26, Outside=27, Specimens=28, BoilerRoom=29)

SpawnFlags = Enum(Byte, Empty=0, PlayerControlled=1)
SpawnId = Enum(PackedInt, ShipStatus=0, MeetingHub=1, Lobby=2, GameData=3, Player=4, HeadQuarters=5, PlanetMap=6,
               AprilShipStatus=7)

MeetingHud_State = Enum(Byte, Discussion=0, NotVoted=1, Voted=2, Results=3, Proceeding=4)
