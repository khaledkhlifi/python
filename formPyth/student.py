class student:

    def __init__(self,CIN, name, nickName ,classe):
        self.CIN = CIN
        self.name = str(name)
        self.nickName = str(nickName)
        self.classe = str(classe) 

    def display(self):
        print("the student "+self.name+" "+self.nickName+" the holder of the CIN : "+self.CIN+" study in " +self.classe)