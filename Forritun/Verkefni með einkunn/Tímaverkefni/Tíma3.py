#Lárus Ármann Kjartansson
#26/11/2020
import random
import re

class Frumklasi():
    def __init__(self,nafn,kyn): 
        self.nafn = nafn 
        self.kyn = kyn
    def __str__(self): 
        return str(self.nafn)+" "+str(self.kyn)
class Annarklasi(Frumklasi):
    def __init__(self, nafn, kyn, heimilisfang, gsm):
        Frumklasi.__init__(self,nafn,kyn)
        self.heimilisfang = heimilisfang
        self.gsm = gsm
    def __str__(self): #býr til fall
            return str(self.nafn)+" "+str(self.kyn)+" "+str(self.heimilisfang)+" "+str(self.gsm)


#class Spil():
 #   def __init__(self, tegun, númer):

        
#def adgangur(ord):
 #   sérstafir =['$', '@', '#', '%'] 
  #  while True:
   #     if (len(ord)<8): 
    #        elif not re.search("[a-z]", ord):  
     #           elif not re.search("[A-Z]", ord): 
      #              elif not re.search("[0-9]", ord): 
       #                 elif ord and not ord[:3].islower(): 
        #                    elif ord and not ord[-1].isupper():
         #                       elif not any(char in sérstafir for char in ord):
          #                          elif not any(int(2) for char in ord):
           #                             flag = -1
            #                        else: 
             #                           flag = 0
              #                          print("Þetta aðgangsorð er í lagi")
               #                         break
        
                               #     if flag == -1: 
                                #        print("Þetta aðgangsorð er ekki i lagi")
                                 #       break
        
#    return ord
                                        
                            #if not any(stafir in sérstafir for stafir in ord):
                                #sérstafir =['$', '@', '#', '%', '!', '*']

    







spilin=["H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "H11", "H12", "H13", 
                "T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8", "T9", "T10", "T11", "T12", "T13", 
                "S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10", "S11", "S12", "S13", 
                "L1", "L2", "L3", "L4", "L5", "L6", "L7", "L8", "L9", "L10", "L11", "L12", "L13",]
      
      
#ord=input("Passorð ")  
#pas=adgangur(ord)
#print(pas)

notandi=[]
for x in range(25):
    randomspil=random.choice(spilin)
    notandi.append(randomspil)
#print("Spil Notenda: ",notandi)

talva=[]
for x in range(25):
    randomspil=random.choice(spilin)
    talva.append(randomspil)
#print("Spil Tölvu: ",talva)

Nafn = input("Nafn")
Kyn = input("kyn")
simanumer = (6261173)
heimilisfang = ("Goðheimar 24")
objekt1 = Frumklasi(Nafn,Kyn)
print(objekt1)
objekt2 = Annarklasi(Nafn,Kyn,simanumer,heimilisfang)
print(objekt2)