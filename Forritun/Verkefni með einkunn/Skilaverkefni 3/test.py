#Lárus Ármann Kjartansson
#19.10.2020
#Skilaverkefni 3

from Nemi import Grunnskolanemi #importar Grunnskólanemi
from Nemi import Framhaldsskolanemi #importar Framhaldsskolanemi
from Nemi import Haskolanemi #importar Haskolanemi


def fjoldiKyn(listi,kyn): #bý til fall sem tekur inn Listan og kyn
    teljari=0 # setur teljarann sem 0
    for nemi in listi: #fyrir nema í listanum
        if kyn == nemi.kyn: #ef kynið er =kynið sem var beðið um
            teljari = teljari + 1 # bætir við einum í teljara
    return teljari # skilar teljaranum

def skolar(listi): #býr til fall sem tekur inn lista
    skolalisti=[] #listi
    for skoli in listi: #for lykkja
        if skoli.nafnSkola not in skolalisti: # ef nafn skólans hefur ekki komið fram áður
            skolalisti.append(skoli.nafnSkola) # færir það skólanafn í listan
        
    return skolalisti # returnar listan með skólunum
             
def nemarIskola(listi, skoliNafn): #býr til fall sem tekur inn lista og skólanafn
    nemendalisti=[] # listi
    for nemi in listi: #for lykkja
        if nemi.nafnSkola == skoliNafn: #ef valið nafn ur valmyndini er í "skoliNafn"
            nemendalisti.append(nemi) #færir nemana sem eru í þeim skóla í listan
    return nemendalisti #skilar listanum

def fjoldiAfanga(listi, fjoAfanga): #býr til fall sem tekur inn lista og fjöldi áfanga
    afangaListi=[] #listi
    for nemi in listi: # for lykkja
        if nemi.fjAfanga <= fjoAfanga: #ef nemandi eru í færri en 4 afangum
            afangaListi.append(nemi) # færir í lista 
    return afangaListi #skilar afangalisti

def bondaFolk(listi): #býr til fall sem tekur inn lista
    utanbæjarListi=[] #listi
    for nemi in listi: #for
        if nemi.postnmr >= 300: #ef postnmr er hærra en 300
            utanbæjarListi.append(nemi) #færir í lista
    return utanbæjarListi #skilar utanbæjarlista

def skuldaNemendur(listi): #býr til fall sem tekur inn lista
    skuldarlisti=[] #listi
    for nemi in listi: #for lykkja
        if nemi.namslan == True: #ef nemi er með namslan 
            skuldarlisti.append(nemi) #færir í lista
    return skuldarlisti #skilar lista með öllum sem eru í skuld

def heildarSkuld(listi): #býr til fall sem tekur inn lista
    summa=0 #teljari
    for nemi in listi: #for lykkja
        if nemi.namslanSkuld > 0: #ef nemi er með skuld
            summa = summa + nemi.namslanSkuld # bætir við skuld nemenda í summu
    return summa #skilar summuni

grunnskolanemar = [Grunnskolanemi( "230777-3069","Kjartan Pálsson","Karl","104","Hólabrekkuskóli","kjartan.palon@hotmail.com","Páll Bjarnason"), #býr til grunnskólanema
                   Grunnskolanemi( "031103-3040","Lárus Kjartansson","Karl","104","Langholtsskoli","larus.arann@gmail.com","Kjartan Pálsson"), #býr til grunnskólanema
                   Grunnskolanemi( "110810-5281","Styrmir Kjartansson","Karl","104","Langholtsskoli","Styrm.kjartansson@gmail.com","Kjartan Pálsson"), #býr til grunnskólanema
                   Grunnskolanemi( "170376-3079","Laufey Sigurðardóttir","Kona","104","Hríseyjarskóli","laufer@hotmail.com","Sigurður Hólmgrímsson"), #býr til grunnskólanema
                   Grunnskolanemi( "191091-2919","Daníel Guðmundsson","Karl","104","Hólabrekkuskóli","Daníel@hotmail.com","Páll Bjarnason"), #býr til grunnskólanema
                   Grunnskolanemi( "300101-5684","Lilja Sveinssdóttir","Kona","104","Hólabrekkuskóli","Lilja@hotmail.com","Páll Bjarnason"), #býr til grunnskólanema
                   Grunnskolanemi( "011264-3069","Konni Forritunarkennari","Karl","104","Hólabrekkuskóli","Konni@gmail.com","Forritun"), #býr til grunnskólanema
                   Grunnskolanemi( "191003-2920","Sigríður Sverrisdóttir","Kona","104","Hólabrekkuskóli","Sigríður@hotmail.com","Páll Bjarnason"), #býr til grunnskólanema
                   Grunnskolanemi( "120812-3568","Stefán Pálsson","Karl","104","Hólabrekkuskóli","Stefán@hotmail.com","Páll Bjarnason"), #býr til grunnskólanema
                   Grunnskolanemi( "060385-3051","Katrín Björnssdóttir","Kona","104","Hólabrekkuskóli","Katrín@hotmail.com","Páll Bjarnason")] #býr til grunnskólanema

framhaldsskolanemar = [Framhaldsskolanemi( "230777-3069","Kjartan Pálsson","Karl",400,"Tækniskólinn","kjartan.palon@hotmail.com","Tölvubraut",2), #býr til framhaldsskolanema
                    Framhaldsskolanemi( "031103-3040","Lárus Kjartansson","Karl",104,"Menntaskólin við Sund","larus.arann@gmail.com","Tölvubraut",7), #býr til framhaldsskolanema
                    Framhaldsskolanemi( "110810-5281","Styrmir Kjartansson","Karl",104,"Fjölbrautarskólin Ármúla","Styrm.kjartansson@gmail.com","Náttúrufræðibraut",6,True), #býr til framhaldsskolanema
                    Framhaldsskolanemi( "170376-3079","Laufey Sigurðardóttir","Kona",104,"Tækniskólinn","laufer@hotmail.com","Tölvubraut",5), #býr til framhaldsskolanema
                    Framhaldsskolanemi( "191091-2919","Daníel Guðmundsson","Karl",104,"Menntaskólin við Sund","Daníel@hotmail.com","Grafísk miðlun",6), #býr til framhaldsskolanema
                    Framhaldsskolanemi( "300101-5684","Lilja Sveinssdóttir","Kona",605,"Fjölbrautarskólin Ármúla","Lilja@hotmail.com","Náttúrufræðibraut",7), #býr til framhaldsskolanema
                    Framhaldsskolanemi( "011264-3069","Konni Forritunarkennari","Karl",104,"Menntaskólin við Sund","Konni@gmail.com","Tölvubraut",3), #býr til framhaldsskolanema
                    Framhaldsskolanemi( "191003-2920","Sigríður Sverrisdóttir","Kona",740,"Tækniskólinn","Sigríður@hotmail.com","Grafísk miðlun",6,True), #býr til framhaldsskolanema
                    Framhaldsskolanemi( "120812-3568","Stefán Pálsson","Karl",104,"Menntaskólin við Sund","Stefán@hotmail.com","Grafísk miðlun",5), #býr til framhaldsskolanema
                    Framhaldsskolanemi( "060385-3051","Katrín Björnssdóttir","Kona",104,"Tækniskólinn","Katrín@hotmail.com","Náttúrufræðibraut",6)] #býr til framhaldsskolanema

haskolanemar = [Haskolanemi( "230777-3069","Kjartan Pálsson","Karl",400,"Tækniskólinn","kjartan.palon@hotmail.com","grunnnám",0), #býr til haskolanema
                    Haskolanemi( "031103-3040","Lárus Kjartansson","Karl",104,"Menntaskólin við Sund","larus.arann@gmail.com","framhaldsnám",0), #býr til haskolanema
                    Haskolanemi( "110810-5281","Styrmir Kjartansson","Karl",104,"Fjölbrautarskólin Ármúla","Styrm.kjartansson@gmail.com","grunnnám",800000,True), #býr til haskolanema
                    Haskolanemi( "170376-3079","Laufey Sigurðardóttir","Kona",104,"Tækniskólinn","laufer@hotmail.com","grunnnám",0), #býr til haskolanema
                    Haskolanemi( "191091-2919","Daníel Guðmundsson","Karl",104,"Menntaskólin við Sund","Daníel@gmail.com","framhaldsnám",250000,True), #býr til haskolanema
                    Haskolanemi( "300101-5684","Lilja Sveinssdóttir","Kona",605,"Fjölbrautarskólin Ármúla","Lilja@gmail.com","framhaldsnám",0), #býr til haskolanema
                    Haskolanemi( "011264-3069","Konni Forritunarkennari","Karl",104,"Menntaskólin við Sund","Konni@gmail.com","grunnnám",0), #býr til haskolanema
                    Haskolanemi( "191003-2920","Sigríður Sverrisdóttir","Kona",740,"Tækniskólinn","Sigríður@gmail.com","framhaldsnám",550000,True), #býr til haskolanema
                    Haskolanemi( "120812-3568","Stefán Pálsson","Karl",104,"Menntaskólin við Sund","Stefán@hotmail.com","grunnnám",0), #býr til haskolanema
                    Haskolanemi( "060385-3051","Katrín Björnssdóttir","Kona",104,"Tækniskólinn","Katrín@hotmail.com","grunnnám",0)] #býr til haskolanema

on = True # on er True
while on == True: #á meðan on er true keyrir lykkjan
    print("1. Grunnskólanemar") #val
    print("2. Framhaldsskólanemar") #val
    print("3. Háskólanemar") #val
    print("4. Hætta") #val
    val = int(input("Veldu hvað þú vilt gera: ")) #input fyrir val
    
    if val == 1: #ef val == 1/grunnskoli
        on2 = True #on er True
        while on2 == True: # while lykkja
            print("1. Allir") #val
            print("2. Fjöldi Kyn") #val
            print("3. SkólaLeit") #val
            print("4. Hætta") #val
            val2 = int(input("Veldu hvað þú vilt gera: ")) #input fyrir val
            
            if val2 == 1: #ef val == 1
                for nemi in grunnskolanemar: #for lykkja til að prenta nemanda einn nemanda á línu
                    print(nemi) #prentar
            elif val2 == 2: #ef val == 2
                print("Karlar: ",fjoldiKyn(grunnskolanemar,"Karl")) #setur í fallið til að finna hve mörg af hverju kyni
                print("Konur: ",fjoldiKyn(grunnskolanemar,"Kona")) #setur í fallið til að finna hve mörg af hverju kyni
            elif val2 == 3: #ef val == 3 
                teljari=0 #teljari
                valskolar = skolar(grunnskolanemar) #tekur inn alla mismunandi skóla í listanum
                for skoli in valskolar: #prentar skólana einn í hverri línu
                    print(teljari,skoli) #prentar skola með töluni í teljaranum fyrir framan svo hægt sé að velja "info" um skólan
                    teljari = teljari+1 #bætir við einum í teljara
                val3 = int(input("Veldu Skóla: ")) #input
                nemar=nemarIskola(grunnskolanemar,valskolar[val3]) #finnur út hvaða skóla þú valdir
                for nemi in nemar: #for lykkja til að prenta í hverri línu
                    print(nemi) #prentar alla nemendur úr þeim skóla sem var valin
                    
            elif val2 == 4: #ef val == 4
                break #brýtur lykkjuna
            
    elif val == 2: #ef val == 2/framhaldsskoli
        on3 = True #heldur lykkjuni í gangi
        while on3 == True: #while lykkja
            print("1. Allir") #val
            print("2. AfangaFjöldi") #val
            print("3. UtanbæjarFólk") #val
            print("4. Hætta") #val
            val3 = int(input("Veldu hvað þú vilt gera: ")) #input fyrir val
            
            if val3 == 1: #ef val == 1
                for nemi in framhaldsskolanemar: #for lykkja til að prenta í hverri línu
                    print(nemi) #prentar
            elif val3 == 2: #ef val == 2
                afangar = fjoldiAfanga(framhaldsskolanemar, 4) #
                for nemi in afangar: #for lykkja til að prenta í hverri línu
                    print(nemi.afangaUtskrift()) #prentar
                
            elif val3 == 3: #ef val == 3
                bondar = BondaFolk(framhaldsskolanemar) #býr til breytu úr returninu frá Bondafolk fallinu
                for nemi in bondar: #for lykkja til að prenta í hverri línu
                    print(nemi.bondaUtskrift()) #prentar
            
            elif val3 == 4: #ef val == 4
                break #brýtur lykkjuna
            
    elif val == 3: #ef val == 3/háskóli
        on4 = True #heldur lykkjuni gangandi
        while on4 == True: #while lykkja
            print("1. Allir") #val
            print("2. NámsSkuld") #val
            print("3. heildarskuld") #val
            print("4. Hætta") #val
            val4 = int(input("Veldu hvað þú vilt gera: ")) #input fyrir val
            
            if val4 == 1: #ef val == 1
                print("---------------------------------------------------------------") 
                for nemi in haskolanemar: #for lykkja til að prenta í hverri línu
                    print(nemi) #prentar
                print("---------------------------------------------------------------") 
            elif val4 == 2: #ef val == 2
                print("---------------------------------------------------------------") 
                print("allir nemendur sem eru í skuld: ") #
                Skuld = skuldaNemendur(haskolanemar) #tekur inn alla sem eru í skuld og setur þá í breytu
                for nemi in Skuld: #for lykkja til að prenta í hverri línu
                    print(nemi.skuldUtskrift())  #prentar
                print("---------------------------------------------------------------") 
            elif val4 == 3: #ef val == 3
                print("---------------------------------------------------------------") 
                Skuld = heildarSkuld(haskolanemar) #tekur heildarskuld og setur það í breytu
                print("heildarskuld allra nemenda er: ",Skuld,"Kr" ) #prentar
                print("---------------------------------------------------------------") 
    elif val == 4: #ef val == 4
        break #brýtur lykkjuna