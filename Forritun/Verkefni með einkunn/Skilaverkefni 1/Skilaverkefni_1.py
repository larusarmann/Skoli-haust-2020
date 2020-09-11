#Lárus Ármann Kjartansson
#03.09.2020
on = True
while on == True:
    print("1.Dictionary ") 
    print("2.Hopar ") 
    print("3.Lykla vinning")
    print("4.Rugla texti")
    print("5.Haetta")

    val = int(input("Veldu hvað þú villt gera: ")) 

    if val == 1:
        dirt = { "Kopavogur":"200",
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
        while on2 == True:
            print("1. Print Staður")
            print("2. +Postnr og Stað")
            print("3.Eyða stað úr safninu")
            print("4.Breyta Postnr")
            print("5.Haetta")
            val1= int(input("vldu hvad du villt gera: "))
            
            if val1 == 1:
                stad = input("Veldu stað: ")
                x = dirt.get(stad)
                print(stad,"=>",x)
                if stad != dirt:
                    print("Þessi staður er ekki til í safninu")

            elif val1 == 2:
                lykill = input("Please input a key: ") 
                gildi = input("Plesse input a value: ") 
                dirt={lykill:gildi}
            
            elif val1 == 3:
                print(str(dirt))
                delete = input("Veldu stað að eyða: ")
                pop_item = dirt.pop(delete)
                print("Þú eyðir:", str(pop_item))
                print("Eftir eyðslu")
                print(str(dirt))
            
            elif val1 == 4:

                print(str(dirt))
                breyta = input("Hvad viltu breyta: ")
                utskipt = int(input("Breyta i >: "))
                dirt[breyta] = utskipt
                print("Eftir breytingu")
                print(str(dirt))
            elif val1 == 5:
                on1 = False
            else:
                on1 = False
    elif val == 2:
        #############
        nafnForr = []
        nafnVesm = []
        nemendurForr = int(input("hve margir eru skráðir í hópinn FORR2HF05CU:"))
        nemendurVesm = int(input("hve margir eru skráðir í hópinn VESM1VS05AU:"))
        
        for x in range(nemendurForr):
            nemandiForr = input("Forr Nafn: ")
            nafnForr.append(nemandiForr)
        #############
        for x in range(nemendurVesm):
            nemandiVesm = input("Vesm Nafn: ")
            nafnVesm.append(nemandiVesm)
        ### Forr
        nafnForr.sort()
        nafnVesm.sort()
        print("Óraðaður listi",nafnForr)
        print("Raðaður listi",nafnForr)
        ### Vesm
        print("Óraðaður listi",nafnVesm)
        print("Raðaður listi",nafnVesm)
        print("\n *** Forritun ***\n")
        for elem in nafnForr:
            print(elem)
        print("\n *** Verksmiðja ***\n")
        for elem in nafnVesm:
            print(elem)
        forr = len(nafnForr)
        vesm = len(nafnVesm)
        if forr < vesm:
            print("Verksmiðja er stærri")
        elif vesm < forr:
            print("Forritun er stærri")        
        else:
            print("Hóparnir eru janfn stórir")

        fjar1 = nafnForr.pop(-2)
        fjar2 = nafnForr.pop(-1)
        
        nafnVesm.append([fjar1,fjar2])
        print("FORR",nafnForr)
        print("VESM",nafnVesm)
    
    elif val == 3:
        username = input("Please enter your username:")
        password = input("Please enter your password:")  
        isMember = False
        isLoggedIn = False
        isPassword = False
        with open('Forritun\Verkefni með einkunn\Skilaverkefni 1\Lyklar.txt','r',encoding = 'utf-8') as f:
            for line in f: 
                x = line.rstrip().split(";")
                if username == x[0]:
                    isMember = True
                
                if username == x[0] and password == x[1]:
                    isLoggedIn = True
                    
                if password == x[1]:
                    isPassword = True
                
            if isLoggedIn == True:
                print("Þú ert meðlimur")
            elif isMember or isPassword:
                print("Það er eitthvað rangt annað hvort nafn eða lykilorð")
            else:
                print("Þú ert ekki meðlimur")
                    
    elif val == 4: 
        word = input("put word:")
        loksins = ''.join([ word[x:x+2][::-1] for x in range(0, len(word), 2) ]) 
        loksins2 = loksins.lower()
        print(loksins2)
        valkost = input("viltu afkoda ja/nei:")
        if valkost == "ja":
            afkodad = ''.join([ loksins[x:x+2][::-1] for x in range(0, len(loksins), 2) ]) 
            print(afkodad)
        elif valkost == "nei":
            break
        
        
    else:
        on = False 
