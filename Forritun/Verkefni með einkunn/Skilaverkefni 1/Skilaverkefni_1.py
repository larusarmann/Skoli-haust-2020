#Lárus Ármann Kjartansson
#03.09.2020
on = True
while on == True: #while lykkja fyrir valmynd
    print("1. Dictionary ") 
    print("2. Forr og Vesm Hópar ") 
    print("3. Skráarvinssla")
    print("4. Víxla texta")
    print("5.Hætta")

    val = int(input("Veldu hvað þú villt gera: ")) 

    if val == 1:
        Dictionary = { "Kopavogur":"200", #dictionary með svæðum og postnmr
                 "Miðborg":"100",
                 "Laugardalur":"104",
                 "Vesturbær":"107",
                 "Breiðholt":"111",
                 "Seltjarnarnes":"170",
                 "Grafarvogur":"112",
                 "Hlíðar":"105",
                 "Garðabær":"210",
                 "Hafnarfjörður":"220"}

        on2 = True
        while on2 == True: #Valmynd 2
            print("1. Prenta Staði")
            print("2. Bæta vip Postnúmer og Stað")
            print("3. Eyða stað úr safninu")
            print("4. Breyta Postnúmer")
            print("5.Hætta")
            val1= int(input("veldu hvað þú vilt gera: "))
            
            if val1 == 1:
                stad = input("Veldu stað: ") #input
                x = Dictionary.get(stad) #finnur staðin í dictionarynu
                print(stad,"=>",x)#prentar stað og pstnmr tengt við staðin
                if stad != Dictionary: # ef input er ekki í dictionaryinu
                    print("Þessi staður er ekki til í safninu")

            elif val1 == 2:
                lykill = input("Nafn á svæðinu: ") #input
                gildi = input("Póstnúmer: ") #input
                Dictionary={lykill:gildi} #bætir við staki í dictionaryið
            
            elif val1 == 3:
                print(str(Dictionary)) #prentar út
                eyða = input("Veldu stað til að eyða: ") #tekur input
                pop_item = Dictionary.pop(eyða) #eyðir stað og postnmr þess
                print("Þú eyðir:", str(pop_item)) #prentar það sem þú eyddir
                print("Eftir: ") #dictionaryið eftir
                print(str(Dictionary)) #dictionaryið eftir
            
            elif val1 == 4:

                print(str(Dictionary)) #prentar dictionaryið
                breyta = input("Hvað viltu breyta: ") #input breyta úr
                SkiptaUt = int(input("Breyta í >: ")) #input breyta í
                Dictionary[breyta] = SkiptaUt #breytir frá dictionary í input
                print("Eftir breytingu") #prentar eftir
                print(str(Dictionary)) #prentar út
            elif val1 == 5:
                break
            else:
                break

    elif val == 2:
        nafnForr = [] #listi
        nafnVesm = [] #listi
        nemendurForr = int(input("Hvað eru margir í hópinum FORR2HF05CU:")) #input
        nemendurVesm = int(input("Hvað eru margir í hópinum VESM1VS05AU:")) #input
        
        for x in range(nemendurForr): #For lykkja
            nemandiForr = input("Nafn Forritun: ") #input
            nafnForr.append(nemandiForr) #færir nöfnin í Forritunarhópin
    
        for x in range(nemendurVesm):
            nemandiVesm = input("Nafn Verksmiðju: ") #input
            nafnVesm.append(nemandiVesm) #færir nöfnin í Verksmiðjuhópin
        #Forritunar hópur
        nafnForr.sort() #Raðar forritunarhópin
        nafnVesm.sort() #Raðar verksmiðjuhópin
        print("Óraðaður listi",nafnForr) #prentar óraðaðan lista
        print("Raðaður listi",nafnForr) #prentar raðaðan lista
        #Verksmiðju hópur
        print("Óraðaður listi",nafnVesm) #prentar óraðaðan lista
        print("Raðaður listi",nafnVesm) #prentar raðaðan lista
        print("\nForritun\n")#prentar
        for elem in nafnForr: #For lykkja prentar forritunarhóp eitt nafn í hverri línu
            print(elem)#prentar
        print("\nVerksmiðja\n")#prentar
        for elem in nafnVesm: #For lykkja prentar Verksmiðjuhóp eitt nafn í hverri línu
            print(elem)#preantar
        forr = len(nafnForr) #finnur lengd forr
        vesm = len(nafnVesm) #finnur lengd Vesm
        if forr < vesm:#ef það eru fleiri í vesm hópinum
            print("Verksmiðja er stærri hópurinn") #prentar
        elif vesm < forr: #ef það eru fleiri í forr hópinum
            print("Forritun er stærri hópurinn") #prentar 
        else: #annars eru þeir jafn stórir
            print("Hóparnir eru janfn stórir") #prentar

        x = nafnForr.pop(-2) #eyðir næst seinasta nafninu í listanum
        x2 = nafnForr.pop(-1) #eyðir seinasta nafninu í listanum
        
        nafnVesm.append([x,x2]) #færir nöfnin í hinn listan
        print("Forritun",nafnForr) #prentar
        print("Verksmiðja",nafnVesm) #prentar
    
    elif val == 3:
        username = input("stimplaðu inn notendanafn:") #tekur inn notendanafn
        password = input("stimplaðu inn lykilorð:") #tekur inn lykilorð
        isMember = False #setur deafaultið í False
        isLoggedIn = False #setur deafaultið í False
        isPassword = False #setur deafaultið í False
        with open('H:\Git\Skoli-haust-2020\Forritun\Verkefni með einkunn\Skilaverkefni 1\Lyklar.txt','r',encoding = 'utf-8') as f: #opnar Texta skjalið með notendanöfnunum
            for line in f: 
                x = line.rstrip().split(";") #splittar línuni í tvennt á ";" og tekur \n úr línuni
                if username == x[0]: #ef notendanafn matchar eitthvað í listanum
                    isMember = True #Breytir í False
                
                if username == x[0] and password == x[1]: #ef notendanafn og passorð matchar þá loggar það inn
                    isLoggedIn = True #Breytir í False
                    
                if password == x[1]: #ef notendanafn matchar eitthvað í listanum
                    isPassword = True #Breytir í False
                
            if isLoggedIn == True: #fer í gegnum if og prentar það sem passar við notendanöfn/passorð
                print("Þú ert meðlimur") #prentar
            elif isMember or isPassword: #fer í gegnum if og prentar það sem passar við notendanöfn/passorð
                print("Það er eitthvað rangt annað hvort nafn eða lykilorð") #prentar
            else: #fer í gegnum if og prentar það sem passar við notendanöfn/passorð
                print("Þú ert ekki meðlimur") #prentar
                    
    elif val == 4: 
        word = input("Skrifaðu orð:") #input
        breytt = ''.join([ word[x:x+2][::-1] for x in range(0, len(word), 2) ]) #afkóðar orðir með því að víksla alltaf 2 stöfum í einu.
        print(breytt.lower()) #prentar
        valkost = input("viltu afkóða orðið ja/nei:") #spyr hbort þú viljir afkóða textann
        if valkost == "ja": #ef þú velur já
            afkodad = ''.join([ breytt[x:x+2][::-1] for x in range(0, len(breytt), 2) ]) #afkóðar orðir með því að víksla alltaf 2 stöfum í einu.
            print(afkodad) #prentar
        elif valkost == "nei": #ef þú velur nei við valkostinum
            break #slekkur á kóðanum
        
        
    else: #ananrs slökknar á forrutinu
        on = False 