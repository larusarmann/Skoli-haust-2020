#Lárus Ármann Kjartansson
#03.09.2020
import math

class FyrstiKlasi:
    #Fyrsti Klassinn sem ég gero á þessari önn
    def fyrra_fall(self,nafn,aldur):
        print("Hallo", nafn,"Þú ert",aldur,"LOL")
    def seinna_fall(self,t1,t2):
        if t1<t2:
            mismunur = t2-t1
        elif t1<t2:
            mismunur=t1-t2
        else:
            mismunur=0
        return "Fjöldi talna milli talnanna er" +str(mismunur-1)

class ThridjiKlasi():
    def __init__(self,tala1,tala2):
        self.tala1=tala1
        self.tala2=tala2

    def summa(self):
        return self.tala1+self.tala1
    def margfalda(self):
        return self.tala1*self.tala2
    def deiling(self):
        return self.tala2/self.tala1

            
#Aðal forrit
#Unnið með fyrsta klas
nafn=input("Hvað heitir þú? ")
aldur=(int(input("Hvað er notandinn gamall: ")))            
tala1=int(input("Sláðu inn tölu 1: "))
tala2=int(input("Sláðu inn tölu 2: "))
konni = FyrstiKlasi()#Bý til hlut úr klasanum FyrstiKlasi sem heitir konni
konni.fyrra_fall(nafn,aldur)#Svona er kallað í aðferð  sem er með print skipun í sér ekki return
print(konni.seinna_fall(tala1,tala2))
#Unnið með þriðja klasi
hlutur=ThridjiKlasi(tala1,tala2)
print("summa talnanna er", hlutur.summa())
print("margföldun talnanna er", hlutur.margfalda())
print("Deiling talnanna er", round(hlutur.deiling()))