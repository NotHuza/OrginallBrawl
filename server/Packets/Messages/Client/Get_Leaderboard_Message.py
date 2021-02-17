from Packets.Messages.Server.Leaderboard.Top_Global_Players_Data_Message import GetLeaderboardGlobalOkMessage
from Packets.Messages.Server.Leaderboard.Top_Local_Players_Data_Message import GetLeaderboardLocalOkMessage
from Packets.Messages.Server.Leaderboard.Top_Global_Clubs_Data_Message import GetLeaderboardClubGlobalOkMessage
from Packets.Messages.Server.Leaderboard.Top_Local_Clubs_Data_Message import GetLeaderboardClubLocalOkMessage

from database.DataBase import DataBase

from Utils.Reader import BSMessageReader


class GetLeaderboardMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.is_local = self.read_Vint()
        self.type = self.read_Vint()
        print(self.is_local, self.type, self.read_int())



    def process(self, crypter):
        if self.type == 1:

            if self.is_local == 1 or self.type == 0:
                GetLeaderboardLocalOkMessage(self.client, self.player).send(crypter)
            else:
                GetLeaderboardGlobalOkMessage(self.client, self.player).send(crypter)


        elif self.type == 2:
            if self.is_local == 1:
                GetLeaderboardClubLocalOkMessage(self.client, self.player, self.type).send(crypter)
            else:
                GetLeaderboardClubGlobalOkMessage(self.client, self.player, self.type).send(crypter)
