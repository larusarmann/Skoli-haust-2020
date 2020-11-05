#Lárus Ármann Kjartansson
#5.11.2020
#Tímaverkefni 2


class Solkerfid():
    def __init__(self,nafn,aldur):
            self.nafn = nafn
            self.aldur = aldur
            self.fjReykistjarna = "10"
    
    def __str__(self):
        return self.nafn+" ; "+self.aldur+" ; "+ self.fjReykistjarna
            
class Jupiter(Solkerfid): 
    def __init__(self,nafn,aldur,radius,tunglaListi):
        Solkerfid.__init__(self,nafn,aldur)
        self.radius = radius
        self.tunglaListi = tunglaListi
    
    def __str__(self):
        str1 = self.nafn+" ; "+self.aldur+" ; "+self.radius+" ; "
        for tungl in jupiterlisti:  
            str1 += tungl 
        return str1
            
        
    
    def skilaStrengur(self):
        return self.nafn+" ; "+self.aldur+" ; "+self.radius
        
class Uranius(Solkerfid):
    def __init__(self,nafn,aldur,radius,tunglaListi):
        Solkerfid.__init__(self,nafn,aldur)
        self.radius = radius
        self.tunglaListi = tunglaListi
    
    def __str__(self):
        str2 = self.nafn+" ; "+self.aldur+" ; "+self.radius+" ; "
        for tungl in uranuslisti:  
            str2 += tungl 
        return str2

class Io(Jupiter):
    def __init__(self,nafn,aldur,radius,tunglaListi):
        Jupiter.__init__(self,nafn,aldur,radius,tunglaListi)
    
    def __str__(self):
        return self.nafn+" ; "+self.aldur+" ; "+self.radius
        
class Evropa(Jupiter):
    def __init__(self,nafn,aldur,radius,tunglaListi):
        Jupiter.__init__(self,nafn,aldur,radius,tunglaListi)
    
    def __str__(self):
        return self.nafn+" ; "+self.aldur+" ; "+self.radius
    

jupiterlisti=["Íó","  ", "Evrópa","  ", "Ganýmedes","  ", "Kallistó"]
uranuslisti=["Míranda","  ", "Aríel","  ", "Úmbríel","  ", "Títanía","  ", "Óberon"]
    
solkerfid = [Solkerfid( "Sólkerfið","10000000000 ára",)]
jupiter = [Jupiter( "Júpiter","4,503E9 ára","69.911 km Radíus",jupiterlisti)]
uranius = [Uranius( "Úraníus","4,503E9 ár","25.362 km Radíus",jupiterlisti)]
io = [Io("Íó","4.5B ára","1,821 km Radíus",jupiterlisti)]
evropa = [Evropa( "Evrópa","4.5B ára","670900 km Radíus",jupiterlisti)]


for x in solkerfid:
    print(x)
for a in jupiter:
    print(a)
for s in uranius:
    print(s)
for b in io:
    print(b)
for v in evropa:
    print(v)