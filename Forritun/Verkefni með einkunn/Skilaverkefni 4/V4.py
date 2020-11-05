#Lárus Ármann Kjartansson
#5.11.2020

import random
#### KLASAR ####
#### TRAPEZOID CLASS ###
class Trapisa:
    numer = 1
    def __init__(self,a=0.0,b=0.0,c=0.0,d=0.0,h=0.0):
        self.a = a 
        self.b = b
        self.c = c
        self.d = d
        self.h = h
        self.nafn = "NN"
        self.numer=Trapisa.numer 
        Trapisa.numer +=1
    def get_a (self):
            return self.a
    def set_a (self,hlid):
            self.a = hlid
    def get_b (self):
            return self.b
    def set_b (self,hlid):
            self.b = hlid
    def get_c (self):
            return self.c
    def set_c (self,hlid):
            self.c = hlid
    def get_d (self):
            return self.d
    def set_d(self,hlid):
            self.d = hlid
    def get_h (self):
            return self.h
    def set_h(self,hlid):
            self.h = hlid

     ### GETTER OG SETTER ###
    def get_nafn (self):
        return self.nafn
    def set_nafn (self,nafn=""):
        self.nafn = nafn
    ### adferdina ###  
    def ummal_trapisa(self):
        return self.a + self.b + self.c + self.d
    def flatarmal_trapisa1(self):
        s=(self.a+self.b+self.c+self.d)/2
        #return (self.a + self.c)/(self.a + self.c)*math.sqrt((s-self.c)*(s-self.a)*
    def flatarmal_trapisa2(self):
        return self.h*((self.a+self.c)/2)
    def trapisa_jafnarma(self):
        if self.d==self.b:
            return True
        else:
            return False
    def __str__(self):
        return "Ég er númer"+str(self.numer)+"og heiti ",self.nafn+"Trapisa eða hálfsamsíðungur er ferhyrningur þar sem tvær mótlægar hliðar eru samsíða."
#### FROG CLASS ####
class Frog:
    numer = 1
    def __init__(self,kyn):
        self.kyn = kyn
        self.numer = Frog.numer
        Frog.numer +=1
    def __str__(self):
        return "I am frog number "+str(self.numer)+" and i am "+self.kyn 
#### CAR CLASS ####
class Car:
    def __init__(self,tegund="",argerd="",hradi=0,bensin=0,eydsla=0):
        self.tegund = tegund
        self.argerd = argerd 
        self.hradi = hradi
        self.bensin = bensin
        self.eydsla = eydsla
    
    def stada(self,sek):
        kominn_metrar=self.hradi*sek
        return kominn_metrar

    def eftir_bensin(self,sek):
        eftir_bensin = (self.bensin-(self.eydsla*self.hradi*sek)/100)
        return eftir_bensin

    def __str__(self):
        return self.tegund+" argerd " +str(self.argerd)

####  Class ####

class Boydem():
    ### klasi fyrir Idrottamenn
    def __init__(self,nafn="",aldur=0,kyn="hk"):
        self.nafn = nafn
        self.aldur = aldur
        self.kyn = kyn
        self.gildi=5
    def kraftur(self):
        return self.gildi

    def __str__(self):
        if self.kyn.lower() =="kk":
            return self.nafn+" er "+str(self.aldur)+" ara gamall"
        else:
            return self.nafn+" er "+str(self.aldur)+" ara gomul"

class Runner(Boydem):
    # Klasi fyrir Hlaupara
    def __init__(self,nafn,aldur,kyn,hradi):
        Boydem.__init__(self,nafn,aldur,kyn)
        self.hradi = hradi
    def kraftur(self):
        return self.gildi*self.hradi 

    def __str__(self):
        if self.kyn.lower() =="kk":
            return self.nafn+" "+str(self.aldur)+" ara gamall og hradinn er "+str(self.hradi)
        else:
            return self.nafn+" "+str(self.aldur)+" ara gomul og hradinn er "+str(self.hradi)


on = True
while on == True:
    print("1.Trapisa")
    print("2.Frog")
    print("3.Car")
    print("4.Erfdir")
    print("5.Haetta")
    val = int(input("Veldu?"))
    if val == 1:
        #### TRAPISA OUTPUT ####
        konni = Trapisa(1,2,3,4,5)
        print(konni.get_a())#1
        konni.set_a(222)
        print(konni.get_a())#222
        konni.set_nafn(input("Nafn? "))
        print(konni.get_nafn())
    elif val == 2:
        #### FROG OUTPUT ####
        dude = Frog("KK")
        print(dude)
        kerling = Frog("KVK")
        print(kerling)
        Frogs_KK =[]
        Frogs_KK.append(dude)
        Frogs_KVK =[]
        Frogs_KVK.append(kerling)
        dagur = 0
        kyn=""
        while (len(Frogs_KVK)+len(Frogs_KK)) < 10000:
            for x in range(len(Frogs_KVK)):
                tala=random.randint(0,1)
                if tala==1:
                    kyn="KK"
                    froskur = Frog(kyn)
                    Frogs_KK.append(froskur)
                else:
                    kyn="KVK"
                    froskur = Frog(kyn)
                    Frogs_KVK.append(Frog)
            dagur+=2
            print("Dagur numer", dagur)
            print("Fjoldi karlfroska er kominn upp i ", len(Frogs_KK))
            print("Fjoldi kvennfroska er kominn upp i ", len(Frogs_KVK))
        print("Detta eru allir karlfroskarnir")
        for Frog in Frogs_KK:
            print(froskur)

    elif val == 3:
        #### CAR OUTPUT ####
        hradi = random.randint(5,15)
        bensin = random.randint(50,200)
        eydsla = random.randint(2,8)
        bill1=Car("Pegassi Zentorno","2016",hradi,bensin,eydsla)
        print(bill1)
        hradi = random.randint(4,14)
        bensin = random.randint(50,200)
        eydsla = random.randint(2,8)
        bill2=Car("Maybach","2012",hradi,bensin,eydsla)
        print(bill2)
        hradi = random.randint(6,16)
        bensin = random.randint(5,200)
        eydsla = random.randint(3,8)
        bill3=Car("Toyota Yaris","2007",hradi,bensin,eydsla)
        print(bill3)
        # BEGIN
        sek = 0 
        while (bill1.stada(sek)<1000 and bill1.eftir_bensin(sek) >=0):
            sek+=1
            print (bill1.tegund,"er kominn",bill1.stada(sek))
            print (bill1.tegund,"a eftir af bensini",round(bill1.eftir_bensin(sek),2))
        sek=0
        
        while (bill2.stada(sek)<1000 and bill2.eftir_bensin(sek) >=0):
            sek+=1
            print (bill2.tegund,"er kominn",bill2.stada(sek))
            print (bill2.tegund,"a eftir af bensini",round(bill2.eftir_bensin(sek),2))
        sek=0

        while (bill3.stada(sek)<1000 and bill3.eftir_bensin(sek) >=0):
            sek+=1
            print (bill3.tegund,"er kominn",bill3.stada(sek))
            print (bill3.tegund,"a eftir af bensini",round(bill3.eftir_bensin(sek),2))
        sek=0
    elif val == 4:
        ob1 = Boydem("Karl",17,"kk")
        print(ob1)
        print(ob1.__doc__)
        ob2 = Runner("Gellan",17,"kvk","5")
        print(ob2)
        print(ob2.__doc__)
        print(ob2.kraftur())


    elif val == 5:
        print("Bless bless")
        break
    else:
        break