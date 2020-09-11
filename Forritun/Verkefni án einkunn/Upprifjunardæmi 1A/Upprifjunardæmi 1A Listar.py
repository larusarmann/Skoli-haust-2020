
import random

def Ord(strengur):
    teljari=0
    for i in strengur:
        if(i.isspace()):
            teljari=teljari+1
    print("fjöldi orða er:",teljari + 1)
    return strengur

def fyrstu(strengur):
    print("Fyrstu 5 stafir > ",strengur[0:5])

    return strengur

def sidustu(strengur):
    print("Sidustu 4 stafir > ",strengur[-4:])

    return strengur

def Midju(strengur):
    
    return print("Midjustafurinn",strengur[(len(strengur)-1)//2:(len(strengur)+2)//2])

def breytaS(strengur):
    strengur = strengur.replace("s", "$")
    strengur = strengur.replace("S", "$")
    return print(strengur)

def medaltal(listi):
    medal = sum(listi) / len(listi)
    print("meðaltal listans er:", medal)
    return medal



on = True
while on == True:
    print("1. Strengjarallý") 
    print("2. Listarally") 
    print("3. Hætta")
    val = int(input("Veldu hvað þú villt gera: ")) 

    if val == 1:
        streng = input(str("Sláðu inn streng: "))
        Ord(streng) 
        fyrstu(streng) 
        sidustu(streng) 
        Midju(streng) 
        breytaS(streng)
    
    elif val == 2:
    
        listi = []

        for i in range(0,100):
            x = random.randint(34,68)
            listi.append(x)
        print("listinn óraðaður",listi)
        listi.sort() 
        print("listinn raðaður",listi)
        
        medaltal(listi)
        print("Minnsta talan er:", listi[:1], "og su sttaersta er:", listi[-1:])
        summa = sum(listi)
        while summa >=4500:
            listi.remove(listi[-1])
            summa = sum(listi)
            print("Nu er summan", summa)
        print("Endanleg summa")
        print("Listinn")

        listi2 =[]
        for numer in listi:
            if (numer % 5 !=0):
                listi2.append(numer)
            (listi)
        listi=listi2.copy()
        print("Listinn an tolur sem gang upp i 5: " , listi)

        fjortiulisti = []
        for numer in listi:
            if(numer == 41):
                listi.remove(numer)
                fjortiulisti.append(listi)
        print("Listinn an 41")
        print("41 listinn: ", fjortiulisti)
