from random import choice
from string import ascii_uppercase
from database.DataBase import DataBase
import json

from Logic.Player import Players
from Packets.Messages.Server.KeepAliveServerMessage import KeepAliveServerMessage

from Utils.Reader import BSMessageReader


class LogicSelectSkinCommand(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
            self.read_Vint()
            self.read_Vint()
            self.read_Vint()
            self.read_Vint()
            self.read_Vint()
            self.player.skinID = self.read_Vint()
            self.read_Vint()
            self.read_Vint()
            self.read_Vint()
            self.read_Vint()
            self.read_Vint()
            self.read_Vint()
            self.player.brawlerID = self.read_Vint()
            
    def process(self):
            DataBase.replaceValue(self, 'skinID', self.player.skinID)
            if self.player.brawlerID == 0:
                DataBase.replaceValue(self, 'shellySkin', self.player.skinID)
            elif self.player.brawlerID == 1:
                DataBase.replaceValue(self, 'coltSkin', self.player.skinID)
            elif self.player.brawlerID == 2:
                DataBase.replaceValue(self, 'bullSkin', self.player.skinID)
            elif self.player.brawlerID == 3:
                DataBase.replaceValue(self, 'brockSkin', self.player.skinID)
            elif self.player.brawlerID == 4:
                DataBase.replaceValue(self, 'ricoSkin', self.player.skinID)
            elif self.player.brawlerID == 5:
                DataBase.replaceValue(self, 'spikeSkin', self.player.skinID)
            elif self.player.brawlerID == 6:
                DataBase.replaceValue(self, 'barleySkin', self.player.skinID)
            elif self.player.brawlerID == 7:
                DataBase.replaceValue(self, 'jessieSkin', self.player.skinID)
            elif self.player.brawlerID == 8:
                DataBase.replaceValue(self, 'nitaSkin', self.player.skinID)
            elif self.player.brawlerID == 9:
                DataBase.replaceValue(self, 'dynamikeSkin', self.player.skinID)
            elif self.player.brawlerID == 10:
                DataBase.replaceValue(self, 'elprimoSkin', self.player.skinID)
            elif self.player.brawlerID == 11:
                DataBase.replaceValue(self, 'mortisSkin', self.player.skinID)
            elif self.player.brawlerID == 12:
                DataBase.replaceValue(self, 'crowSkin', self.player.skinID)
            elif self.player.brawlerID == 13:
                DataBase.replaceValue(self, 'pocoSkin', self.player.skinID)
            elif self.player.brawlerID == 14:
                DataBase.replaceValue(self, 'boSkin', self.player.skinID)
            elif self.player.brawlerID == 15:
                DataBase.replaceValue(self, 'piperSkin', self.player.skinID)
            elif self.player.brawlerID == 16:
                DataBase.replaceValue(self, 'pamSkin', self.player.skinID)
            elif self.player.brawlerID == 17:
                DataBase.replaceValue(self, 'taraSkin', self.player.skinID)
            elif self.player.brawlerID == 18:
                DataBase.replaceValue(self, 'darrylSkin', self.player.skinID)
            elif self.player.brawlerID == 19:
                DataBase.replaceValue(self, 'pennySkin', self.player.skinID)
            elif self.player.brawlerID == 20:
                DataBase.replaceValue(self, 'frankSkin', self.player.skinID)
                DataBase.replaceValue(self, 'brawlerID', self.player.brawlerID)