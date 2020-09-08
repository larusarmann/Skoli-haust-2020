# Lárus Ármann Kjartansson
#3.Sep 2020
def word_mixer(word_list):
    new_words = []
    word_list.sort()
    while(len(word_list) > 5):
        new_words.append(word_list.pop(-5))
        new_words.append(word_list.pop(0))
        new_words.append(word_list.pop(-1))
        new_words.append('\n')
    return(new_words)

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
        print("Óraðaður listi",nofnForr)
        print("Raðaður listi",sorted(nofnForr))
        ### Vesm
        print("Óraðaður listi",nofnVesm)
        print("Raðaður listi",sorted(nofnVesm))
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
        
        
        #nofnForr.pop(-0)
        #nofnForr.pop(-1)
        
        

    elif val == 3:
        str = input('Sláðu inn setningu: ')
        wordlist = str.split()
        for i in range(len(wordlist)):
            if len(wordlist[i]) < 4:
                wordlist[i] = wordlist[i].lower()
            if len(wordlist[i]) > 6:
                wordlist[i] = wordlist[i].upper()
        if len(wordlist) > 5:
            newlist = word_mixer(wordlist)
            #print(newlist)
            for i in range(len(newlist)):
                print(newlist[i], end=' ')
    elif val == 4:
        on = False