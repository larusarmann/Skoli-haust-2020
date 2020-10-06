import csv
from klasi import Verkalydsfelag

verkalydsfelag = []
def opnaskra():
    with open("Forritun/Verkefni með einkunn/Skilaverkefni 3/verkalydsfelag.csv" ,'r',newline='',encoding='utf-8') as file:
        reader = csv.reader(file,delimiter=';')
        print(reader)
        for row in reader:
            #print(row)
            hlutur = Verkalydsfelag(row[0],row[1],row[2],row[3])
            verkalydsfelag.append(hlutur)
          
def skrifaSkra(): #Skrifar í skrána.
    if len(verkalydsfelag) == 0:
        print('--Listi tomur--')
    else:
        with open('Forritun/Verkefni með einkunn/Skilaverkefni 3/verkalydsfelag.csv','w', newline='',encoding='utf-8') as file:
            writer = csv.writer(file,delimiter=';',quotechar='"',quoting=csv.QUOTE_MINIMAL)
            for x in verkalydsfelag:
                writer.writerow([x.nafn,x.felagsnumer,x.laun,x.kennitala])
        print("--Buid ad vista--")

def nyrMedlimur(): #baetir inn nyjum medlimi tilviki (object,hluti)
    
    nyttNafn = input("Sladu inn nafn a medlimi: ")
    nyttFelagsnumer = input("Sladu inn felagsnumer: ")
    nyttLaun = input("Sladu inn laun: ")
    nyttKennitala = input("Sladu inn kennitala: ")
    nyrHlutur = Verkalydsfelag(nyttNafn,nyttFelagsnumer,nyttLaun,nyttKennitala) # bý til nýtt object 
    verkalydsfelag.append(nyrHlutur) # set hlutinn i lista
    print("--Nyr medlimur hefur verid skradur, a eftir ad skrifa i skranna--")

def eydaMedlimi(eydaNafn,numer): #eyðir tilvikiobject,hluti
    for x in verkalydsfelag:
        if str(x.felagsnumer) == numer and str(x.nafn) == eydaNafn:
            verkalydsfelag.remove(x)
            return eydaNafn+"hefur verid eytt" 
        else:
            return "Ekki tókst að eyða"+eydaNafn+"ur skranni. Nafn og felagsnumer passar ekki. Reyndu aftur sidar"


def breytaMedlimi(breytaNafn,numer): #breytir tilviki(object,hluti)
     for x in verkalydsfelag:
        if str(x.felagsnumer) == numer and str(x.nafn) == breytaNafn:
            verkalydsfelag.replace(x)
            return breytaNafn+"hefur verid breytt" 
        else:
            return "Ekki tókst að breyta"+breytaNafn+"ur skranni. Nafn og felagsnumer passar ekki. Reyndu aftur sidar"


def prentaVerkalydsfelag(): #skrifar á skjáinn allt sem er í skránni(innhald listans af tilvikum)
    pass

def nafnLaun():#skrifar á skjáinn nafn og laun hvers meðlimar fyrir sig.
    pass

def utborgudlaun(): #Útborguð laun hvers meðlimar verkalýðsfélagsins heildarskattar(): skrifar á skjáinn heildarskatta allra meðlima verkalýðsfélagsins
    pass

def mittFall(): #nefnið fallið einhverju lýsandi nafni
    pass


flag=True
while flag:
    print('1.Syna skra')
    print('2.Baeta vid medlim ')
    print('3.Eyda ut med')
    print('4.Breyta upplys')
    print('5.Nafn og heildarlaun')
    print('6.Utborgud laun')
    print('7.Skrifa ut alla sem eru faeddir eftir ????')
    print('8.Skrifa breytingar i skra')
    print('9.Haetta')

    val = input("veldu 1 til 9: ")

    if val == "1":
        for medlimur in verkalydsfelag:
            print(medlimur.prenta_upplysingar_um_medlim())
        print("--buid--")
            
    
    elif val =="2":
        nyrMedlimur()
        
    elif val =="3":
        print("--------------")
        for medlimur in verkalydsfelag:
            print(medlimur.prenta_upplysingar_um_medlim())
        print("--------------")
        eydaNafn = input("Delete the nafn: ")
        numer = input("What is the felagsnumer: ")
        print(eydaMedlimi(eydaNafn,numer))
      
    elif val =="4":
        print("--------------")
        for medlimur in verkalydsfelag:
            print(medlimur.prenta_upplysingar_um_medlim())
        print("--------------")
        breyting = input("Hvað viltu breyta: ")
        numer = input("What is the felagsnumer: ")
        repla = input('what would you change it to: ')
        print(breytaMedlimi(repla,numer))
      

      
    elif val =="5":
        pass
      
    elif val =="6":
        pass
      
    elif val =="7":
        pass
      
    elif val =="8":
        skrifaSkra()
      
    elif val =="9":
        print('--LOL--')
        flag = False




   
