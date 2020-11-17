#Lárus Ármann Kjartansson
#Skilaverkefni 5
#10.11.2020
import random

def randomTolur(tala,byrja,enda): #býr til fall
    listi=[] #býr til lista
    for x in range(tala): #for lykkja
        t1=byrja #
        listi.append(t1) #færir t1 í listan
        byrja+=1 #bætir við í byrja
    return listi #returnar lista

def finnaSamtolu(talnot,listi): #býr til fall
    summa=0 #sett sem 0
    for tala in list: #for lykkja
        if tala % talnot == 0: #if lykkja
            summa+=tala
    return summa #returnar



on = True # on er True
while on == True: #á meðan on er true keyrir lykkjan
    print("1. Dæmi 1") #val
    print("2. Dæmi 2") #val
    print("3. Dæmi 3") #val
    print("4. Dæmi 4") #val
    print("5. Dæmi 5") #val
    print("6. Dæmi 6") #val
    print("7. Dæmi 7") #val
    print("8. Dæmi 8") #val
    print("9. Dæmi 9") #val
    print("0. Hætta") #val
    val = int(input("Veldu hvað þú vilt gera: ")) #input fyrir val
    	
    if val == 1:#val
        print(randomTolur(4,3,20))
    elif val == 2:#val
        listi=randomTolur(100,200,600)
        listi_nyr=list(filter(lambda x:x%2==0,listi))
        print(listi_nyr)
    elif val == 3:#val
        listi1=randomTolur(20,200,400)
        print(listi1)
        listi_nyr2=list(filter(lambda x:x % 5==0 and x>350,listi1))
        print(listi_nyr2)
    elif val == 4:#val
        listi2=[]
        for x in range(200):
            randomtala=random.randint(100,900)
            listi2.append(randomtala)
        print(listi2)
        print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        prentMap = list(map(lambda x: x - 2, listi2))
        print(prentMap)
    elif val == 5:#val
        listi3=[]
        for x in range(200):
            randomtala=random.randint(1,90)
            listi3.append(randomtala)
        print(listi3)
        print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        veld=[x**3 for x in listi3 if x<6]
        print(veld)
    elif val == 6:#val
        listi4=randomTolur(100,1,20)
        print(listi4)
        listi=[x for x in listi4 if str(x)[-1]=="0"]
        print(listi)
    elif val == 7:#val
        x=2
        y=0
        def margfalda(listi):
            if len(listi) == 0:
                return 1
            else:
                return listi[0] * margfalda(listi[1:])
        print(margfalda(listi))
    elif val == 8:#val
        listi=randomTolur(100,200,3000)
        def generator(listi):
            for x in listi:
                yield x
        for item in generator(listi):
            print(item)
    elif val == 9:#val
        on = False
        