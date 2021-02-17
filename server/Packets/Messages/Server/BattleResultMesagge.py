from Utils.Writer import Writer
from database.DataBase import DataBase


class BattleResultMesagge(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 23456
        self.player = player

    def encode(self):
        self.writeVint(2)
        self.writeVint(1)
        self.writeVint(1)#0
        self.writeVint(1)#0
        self.writeVint(1)#0
        self.writeInt(8193)
        self.writeString(self.player.name)
        self.writeVint(1)
        self.writeVint(16)
        self.writeVint(1)#0
        self.writeVint(29)
        self.writeVint(14)#brawl id self.player.selected_brawler
        self.writeVint(9999)
        self.writeVint(10)
        self.writeVint(1)
        self.writeVint(1)
        self.writeVint(1)
        self.writeVint(1)
        self.writeVint(28)
        self.writeVint(1)
        self.writeVint(1)