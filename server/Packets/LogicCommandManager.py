from Packets.Commands.Client.LogicGatchaCommand import LogicGatchaCommand
from Packets.Commands.Client.LogicSelectSkinCommand import LogicSelectSkinCommand
from Packets.Commands.Server.LogicChangeAvatarNameCommand import LogicChangeAvatarNameCommand

commands = {
    #201: LogicChangeAvatarNameCommand,
    500: LogicGatchaCommand,
    506: LogicSelectSkinCommand
}
