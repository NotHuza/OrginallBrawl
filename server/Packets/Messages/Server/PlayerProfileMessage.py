from Utils.Writer import Writer
from database.DataBase import DataBase
from Utils.Helpers import Helpers


class PlayerProfileMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24113
        self.player = player

    def encode(self):
        self.writeVint(0) #HighID
        self.writeVint(1) #LowID
        self.writeString("dsadsad")
        self.writeVint(0)

        self.writeVint(21)#21

        self.writeVint(16)
        self.writeVint(0)#shelly
        self.writeVint(0)
        self.writeVint(9999)
        self.writeVint(9999)
        self.writeVint(10)
                
        self.writeVint(16)
        self.writeVint(8)#nita
        self.writeVint(0)
        self.writeVint(9999)
        self.writeVint(9999)
        self.writeVint(10)
        
        self.writeVint(16)
        self.writeVint(1)#colt
        self.writeVint(0)
        self.writeVint(9999)
        self.writeVint(9999)
        self.writeVint(10)
        
        self.writeVint(16)
        self.writeVint(2)#bull
        self.writeVint(0)
        self.writeVint(9999)
        self.writeVint(9999)
        self.writeVint(10)
                
        self.writeVint(16)
        self.writeVint(7)#jessie
        self.writeVint(0)
        self.writeVint(9999)
        self.writeVint(9999)
        self.writeVint(10)

        self.writeVint(16)
        self.writeVint(3)#brock
        self.writeVint(0)
        self.writeVint(9999)
        self.writeVint(9999)
        self.writeVint(10)
        
        self.writeVint(16)
        self.writeVint(9)#dynimike
        self.writeVint(0)
        self.writeVint(9999)
        self.writeVint(9999)
        self.writeVint(10)
                
        self.writeVint(16)
        self.writeVint(14)#bo
        self.writeVint(0)
        self.writeVint(9999)
        self.writeVint(9999)
        self.writeVint(10)
                
        self.writeVint(16)
        self.writeVint(10)#elprimo
        self.writeVint(0)
        self.writeVint(9999)
        self.writeVint(9999)
        self.writeVint(10)
                
        self.writeVint(16)
        self.writeVint(6)#barley
        self.writeVint(0)
        self.writeVint(9999)
        self.writeVint(9999)
        self.writeVint(10)
        
        self.writeVint(16)
        self.writeVint(13)#pocko
        self.writeVint(0)
        self.writeVint(9999)
        self.writeVint(9999)
        self.writeVint(10)

        self.writeVint(16)
        self.writeVint(4)#ricochet
        self.writeVint(0)
        self.writeVint(9999)
        self.writeVint(9999)
        self.writeVint(10)
                
        self.writeVint(16)
        self.writeVint(18)#darryl
        self.writeVint(0)
        self.writeVint(9999)
        self.writeVint(9999)
        self.writeVint(10)
        
        self.writeVint(16)
        self.writeVint(19)#penny
        self.writeVint(0)
        self.writeVint(9999)
        self.writeVint(9999)
        self.writeVint(10)
        
        self.writeVint(16)
        self.writeVint(15)#piper
        self.writeVint(0)
        self.writeVint(9999)
        self.writeVint(9999)
        self.writeVint(10)
        
        self.writeVint(16)
        self.writeVint(16)#pam
        self.writeVint(0)
        self.writeVint(9999)
        self.writeVint(9999)
        self.writeVint(10)
        
        self.writeVint(16)
        self.writeVint(20)#frank
        self.writeVint(0)
        self.writeVint(9999)
        self.writeVint(9999)
        self.writeVint(10)

        self.writeVint(16)
        self.writeVint(11)#mortis
        self.writeVint(0)
        self.writeVint(9999)
        self.writeVint(9999)
        self.writeVint(10)
        
        self.writeVint(16)
        self.writeVint(17)#tara
        self.writeVint(0)
        self.writeVint(9999)
        self.writeVint(9999)
        self.writeVint(10)

        self.writeVint(16)
        self.writeVint(5)#spike
        self.writeVint(0)
        self.writeVint(9999)
        self.writeVint(9999)
        self.writeVint(10)

        self.writeVint(16)
        self.writeVint(12)#crow
        self.writeVint(0)
        self.writeVint(9999)
        self.writeVint(9999)
        self.writeVint(10)

        self.writeVint(11)

        self.writeVint(1)
        self.writeVint(9999) # Total victories

        self.writeVint(2)
        self.writeVint(2) # Player experience

        self.writeVint(3)
        self.writeVint(self.player.trophies) # Trophies

        self.writeVint(4)
        self.writeVint(self.player.trophies) # Highest trophies

        self.writeVint(5)
        self.writeVint(21) # Brawlers count 21

        self.writeVint(6)
        self.writeVint(0) # Unknown

        self.writeVint(7)
        self.writeVint(self.player.profileIcon) # Profile icon

        self.writeVint(8)
        self.writeVint(9999) # Solo victories

        self.writeVint(9)
        self.writeVint(8) # Best robo rumble time

        self.writeVint(10)
        self.writeVint(9) # Best time as big brawler

        self.writeVint(11)
        self.writeVint(9999) # Duo victories

        self.writeVint(0)
        self.writeVint(0)
        print("[INFO] Message PlayerProfileMessage has been sent.")