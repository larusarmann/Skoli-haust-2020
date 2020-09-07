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
                dirt = {lykill:gildi}
            
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
                on1 = false
            else:
                on1 = False




    elif val == 2:
        pass
    elif val == 3:
        pass
    elif val == 4:
        on = False