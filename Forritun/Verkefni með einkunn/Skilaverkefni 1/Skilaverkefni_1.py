# Lárus Ármann Kjartansson
#3.Sep 2020
# Karl Philip Vallesterol
#3.Sep 2020

on = True
while on == True:
    print("1.Dictionary ") 
    print("2.Hopar ") 
    print("3.Lykla vinning")
    print("4.Haetta")

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
        nofnForr = []
        nofnVesm = []
        nemendurForr = int(input("hve margir eru skráðir í hópinn FORR2HF05CU:"))
        nemendurVesm = int(input("hve margir eru skráðir í hópinn VESM1VS05AU:"))
        
        for x in range(nemendurForr):
            nemandiForr = input("Forr Nafn: ")
            nofnForr.append(nemandiForr)
        #############
        for x in range(nemendurVesm):
            nemandiVesm = input("Vesm Nafn: ")
            nofnVesm.append(nemandiVesm)
        ### Forr
        nofnForr.sort()
        nofnVesm.sort()
        print("Óraðaður listi",nofnForr)
        print("Raðaður listi",nofnForr)
        ### Vesm
        print("Óraðaður listi",nofnVesm)
        print("Raðaður listi",nofnVesm)
        print("\n *** Forritun ***\n")
        for elem in nofnForr:
            print(elem)
        print("\n *** Verksmiðja ***\n")
        for elem in nofnVesm:
            print(elem)
        forr = len(nofnForr)
        vesm = len(nofnVesm)
        if forr < vesm:
            print("Verksmiðja er stærri")
        elif vesm < forr:
            print("Forritun er stærri")        
        else:
            print("Hóparnir eru janfn stórir")

        fjar1 = nofnForr.pop(-2)
        fjar2 = nofnForr.pop(-1)
        
        nofnVesm.append([fjar1,fjar2])
        print("FORR",nofnForr)
        print("VESM",nofnVesm)
    elif val == 3:
        username = input("Please enter your username:")
        password = input("Please enter your password:")  
        with open('Forritun\Lyklar.txt','r',encoding = 'utf-8') as f:
            for line in f: 
                if username + ';' + password + '\n' == line:
                    print('Þú ert meðlimur')
                    break
                else:
                    print('Þú ert ekki meðlimur')
        


    elif val == 4:
        on = False







