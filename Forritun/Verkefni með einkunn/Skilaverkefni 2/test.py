import csv
from klasi import Verkalydsfelag

verkalydsfelag=[]
def opnaskra():
    with open("Verkefni með einkunn/Skilaverkefni 2/verkalydsfelag.csv" ,'r',newline='',encoding='utf-8') as file:
        reader =csv.reader(file,delimiter=';')
        print(reader)
        for row in reader:
            #print(row)
            hlutur = Verkalydsfelag(row[0],row[1],row[2],row[3])
            verkalydsfelag.append(hlutur)
def SkrifaSkra():
    if len(verkalydsfelag) == 0:
        print("listi tómur")
    else:
        with open("Verkefni með einkunn/Skilaverkefni 2/verkalydsfelag.csv",'w',newline='',encoding='utf-8') as file:
            writer = csv.writer(file,delimiter=';',quotechar='"',quoting=csv.QUOTE_MINIMAL)
            for x in verkalydsfelag:
                writer.writerow([x.nafn, x.felagsnumer, x.laun, x.kennitala])
        print("búið að vista")
def nyrmedlimur():
    nyttNafn=input("sláðu inn nafn á meðlimi ")
    nyttFélagsnúmer=input("sláðu inn félagsnúmer ")
    nyttLaun=input("heildarlaun ")
    nyttK+ennitala=input("Kennitala ")
    nyrhlutur=Verkalydsfelag(nyttNafn, nyttFélagsnúmer, nyttLaun, nyttKennitala)
    verkalydsfelag.append(nyrhlutur)
    print("Nýr meðlimur hefur verið skráður")
    

on=True
while on:
    print("1. Sýna skránna")
    print("2. skrifa í skránna")
    print("3. ")
    print("4. ")
    print("5. ")
    print("6. ")
    print("7. ")
    print("8. ")
    print("9. hætta")
    val=int(input("veldu 1 til 9 "))
    
    if val == 1:
        opnaskra()
        for x in verkalydsfelag:
            print(x.prenta_upplysingar_um_medlim())
        print(verkalydsfelag)
    if val == 2:
        nyrmedlimur()
    if val == 3:
        pass
    if val == 4:
        pass
    if val == 5:
        pass
    if val == 6:
        pass
    if val == 7:
        pass
    if val == 8:
        skrifaSkra
    if val == 9:
        on =False
