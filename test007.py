class Player:
    def __init__(self,Name,ID,Level,Exp):
        self.Name = Name
        self.ID = ID
        self.Level = Level
        self.Exp = Exp

    #def __del__(self):
        #print("我被删除了!")

    def Massage(self):
        print ("昵称：%s,玩家ID：%s,玩家等级：%s,玩家经验：%s" % (self.Name,self.ID,self.Level,self.Exp))

    def GetID(self):
        print(self.ID)



Player1 = Player("lukas",15,100,1)

Player1.GetID()
Player1.Massage()

#def __name__ == "__main__"
