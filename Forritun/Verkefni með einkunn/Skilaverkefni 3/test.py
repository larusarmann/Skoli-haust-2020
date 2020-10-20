from Nemi import Grunnskolanemi #importar Grunnskólanemi
from Nemi import Framhaldsskolanemi #importar Framhaldsskolanemi
from Nemi import Haskolanemi #importar Haskolanemi


def fjoldiKyn(listi,kyn): #bý til fall sem tekur inn Listan og kyn
    teljari=0 # setur teljarann sem 0
    for nemi in listi: #fyrir nema í listanum
        if kyn == nemi.kyn: #ef kynið er =kynið sem var beðið um
            teljari = teljari + 1 # bætir við einum í teljara
    return teljari # skilar teljaranum

def skolar(listi): #
    skolalisti=[] #
    for skoli in listi: #
        if skoli.nafnSkola not in skolalisti: #
            skolalisti.append(skoli.nafnSkola) #
        
    return skolalisti #
             
def nemarIskola(listi, skoliNafn): #
    nemendalisti=[] #
    for nemi in listi: #
        if nemi.nafnSkola == skoliNafn: #
            nemendalisti.append(nemi) #
    return nemendalisti #

def fjoldiAfanga(listi, fjoAfanga): #
    afangaListi=[] #
    for nemi in listi: # 
        if nemi.fjAfanga <= fjoAfanga: #
            afangaListi.append(nemi) # 
    return afangaListi #

def bondaFolk(listi): #
    utanbæjarListi=[] #
    for nemi in listi: #
        if nemi.postnmr >= 300: #
            utanbæjarListi.append(nemi) #
    return utanbæjarListi #

def skuldaNemendur(listi): #
    skuldarlisti=[] #
    for nemi in listi: #
        if nemi.namslan == True: #
            skuldarlisti.append(nemi) #
    return skuldarlisti #

def heildarSkuld(listi): #
    summa=0 #
    for nemi in listi: #
        if nemi.namslanSkuld > 0: #
            summa = summa + nemi.namslanSkuld #   
    return summa #

grunnskolanemar = [Grunnskolanemi( "230777-3069","Kjartan Pálsson","Karl","104","Hólabrekkuskóli","kjartan.palon@hotmail.com","Páll Bjarnason"), #
                   Grunnskolanemi( "031103-3040","Lárus Kjartansson","Karl","104","Langholtsskoli","larus.arann@gmail.com","Kjartan Pálsson"), #
                   Grunnskolanemi( "110810-5281","Styrmir Kjartansson","Karl","104","Langholtsskoli","Styrm.kjartansson@gmail.com","Kjartan Pálsson"), #
                   Grunnskolanemi( "170376-3079","Laufey Sigurðardóttir","Kona","104","Hríseyjarskóli","laufer@hotmail.com","Sigurður Hólmgrímsson"), #
                   Grunnskolanemi( "191091-2919","Daníel Guðmundsson","Karl","104","Hólabrekkuskóli","Daníel@hotmail.com","Páll Bjarnason"), #
                   Grunnskolanemi( "300101-5684","Lilja Sveinssdóttir","Kona","104","Hólabrekkuskóli","Lilja@hotmail.com","Páll Bjarnason"), #
                   Grunnskolanemi( "011264-3069","Konni Forritunarkennari","Karl","104","Hólabrekkuskóli","Konni@gmail.com","Forritun"), #
                   Grunnskolanemi( "191003-2920","Sigríður Sverrisdóttir","Kona","104","Hólabrekkuskóli","Sigríður@hotmail.com","Páll Bjarnason"), #
                   Grunnskolanemi( "120812-3568","Stefán Pálsson","Karl","104","Hólabrekkuskóli","Stefán@hotmail.com","Páll Bjarnason"), #
                   Grunnskolanemi( "060385-3051","Katrín Björnssdóttir","Kona","104","Hólabrekkuskóli","Katrín@hotmail.com","Páll Bjarnason")] #

framhaldsskolanemar = [Framhaldsskolanemi( "230777-3069","Kjartan Pálsson","Karl",400,"Tækniskólinn","kjartan.palon@hotmail.com","Tölvubraut",2), #
                    Framhaldsskolanemi( "031103-3040","Lárus Kjartansson","Karl",104,"Menntaskólin við Sund","larus.arann@gmail.com","Tölvubraut",7), #
                    Framhaldsskolanemi( "110810-5281","Styrmir Kjartansson","Karl",104,"Fjölbrautarskólin Ármúla","Styrm.kjartansson@gmail.com","Náttúrufræðibraut",6,True), #
                    Framhaldsskolanemi( "170376-3079","Laufey Sigurðardóttir","Kona",104,"Tækniskólinn","laufer@hotmail.com","Tölvubraut",5), #
                    Framhaldsskolanemi( "191091-2919","Daníel Guðmundsson","Karl",104,"Menntaskólin við Sund","Daníel@hotmail.com","Grafísk miðlun",6), #
                    Framhaldsskolanemi( "300101-5684","Lilja Sveinssdóttir","Kona",605,"Fjölbrautarskólin Ármúla","Lilja@hotmail.com","Náttúrufræðibraut",7), #
                    Framhaldsskolanemi( "011264-3069","Konni Forritunarkennari","Karl",104,"Menntaskólin við Sund","Konni@gmail.com","Tölvubraut",3), #
                    Framhaldsskolanemi( "191003-2920","Sigríður Sverrisdóttir","Kona",740,"Tækniskólinn","Sigríður@hotmail.com","Grafísk miðlun",6,True), #
                    Framhaldsskolanemi( "120812-3568","Stefán Pálsson","Karl",104,"Menntaskólin við Sund","Stefán@hotmail.com","Grafísk miðlun",5), #
                    Framhaldsskolanemi( "060385-3051","Katrín Björnssdóttir","Kona",104,"Tækniskólinn","Katrín@hotmail.com","Náttúrufræðibraut",6)] #

haskolanemar = [Haskolanemi( "230777-3069","Kjartan Pálsson","Karl",400,"Tækniskólinn","kjartan.palon@hotmail.com","grunnnám",0), #
                    Haskolanemi( "031103-3040","Lárus Kjartansson","Karl",104,"Menntaskólin við Sund","larus.arann@gmail.com","framhaldsnám",0), #
                    Haskolanemi( "110810-5281","Styrmir Kjartansson","Karl",104,"Fjölbrautarskólin Ármúla","Styrm.kjartansson@gmail.com","grunnnám",800000,True), #
                    Haskolanemi( "170376-3079","Laufey Sigurðardóttir","Kona",104,"Tækniskólinn","laufer@hotmail.com","grunnnám",0), #
                    Haskolanemi( "191091-2919","Daníel Guðmundsson","Karl",104,"Menntaskólin við Sund","Daníel@gmail.com","framhaldsnám",250000,True), #
                    Haskolanemi( "300101-5684","Lilja Sveinssdóttir","Kona",605,"Fjölbrautarskólin Ármúla","Lilja@gmail.com","framhaldsnám",0), #
                    Haskolanemi( "011264-3069","Konni Forritunarkennari","Karl",104,"Menntaskólin við Sund","Konni@gmail.com","grunnnám",0), #
                    Haskolanemi( "191003-2920","Sigríður Sverrisdóttir","Kona",740,"Tækniskólinn","Sigríður@gmail.com","framhaldsnám",550000,True), #
                    Haskolanemi( "120812-3568","Stefán Pálsson","Karl",104,"Menntaskólin við Sund","Stefán@hotmail.com","grunnnám",0), #
                    Haskolanemi( "060385-3051","Katrín Björnssdóttir","Kona",104,"Tækniskólinn","Katrín@hotmail.com","grunnnám",0)] #

on = True #
while on == True: #
    print("1. Grunnskólanemar") #
    print("2. Framhaldsskólanemar") #
    print("3. Háskólanemar") #
    print("4. Hætta") #
    val = int(input("Veldu hvað þú vilt gera: ")) #
    
    if val == 1: #
        on2 = True #
        while on2 == True: #
            print("1. Allir") #
            print("2. Fjöldi Kyn") #
            print("3. SkólaLeit") #
            print("4. Hætta") #
            val2 = int(input("Veldu hvað þú vilt gera: ")) #
            
            if val2 == 1: #
                for nemi in grunnskolanemar: #
                    print(nemi) #
            elif val2 == 2: #
                print("Karlar: ",fjoldiKyn(grunnskolanemar,"Karl")) #
                print("Konur: ",fjoldiKyn(grunnskolanemar,"Kona")) #
            elif val2 == 3: #
                teljari=0 #
                valskolar = skolar(grunnskolanemar) #
                for skoli in valskolar: #
                    print(teljari,skoli) #
                    teljari = teljari+1 #
                val3 = int(input("Veldu Skóla: ")) #
                nemar=nemarIskola(grunnskolanemar,valskolar[val3]) #
                for nemi in nemar: #
                    print(nemi) #
                    
            elif val2 == 4: #
                break #
            
    elif val == 2: #
        on3 = True #
        while on3 == True: #
            print("1. Allir") #
            print("2. AfangaFjöldi") #
            print("3. UtanbæjarFólk") #
            print("4. Hætta") #
            val3 = int(input("Veldu hvað þú vilt gera: ")) #
            
            if val3 == 1: #
                for nemi in framhaldsskolanemar: #
                    print(nemi) #
            elif val3 == 2: #
                afangar = fjoldiAfanga(framhaldsskolanemar, 4) #
                for nemi in afangar: #
                    print(nemi.afangaUtskrift()) #
                
            elif val3 == 3: #
                bondar = BondaFolk(framhaldsskolanemar) #
                for nemi in bondar: #
                    print(nemi.bondaUtskrift()) #
            
            elif val3 == 4: #
                break #
    elif val == 3: #
        on4 = True #
        while on4 == True: #
            print("1. Allir") #
            print("2. AfangaFjöldi") #
            print("3. UtanbæjarFólk") #
            print("4. Hætta") #
            val4 = int(input("Veldu hvað þú vilt gera: ")) #
            
            if val4 == 1: #
                print("---------------------------------------------------------------") #
                for nemi in haskolanemar: #
                    print(nemi) #
                print("---------------------------------------------------------------") #
            elif val4 == 2: #
                print("---------------------------------------------------------------") #
                print("allir nemendur sem eru í skuld: ") #
                Skuld = skuldaNemendur(haskolanemar) #
                for nemi in Skuld: #
                    print(nemi.skuldUtskrift())  #
                print("---------------------------------------------------------------") #
            elif val4 == 3: #
                print("---------------------------------------------------------------") #
                Skuld = heildarSkuld(haskolanemar) #
                print("heildarskuld allra nemenda er: ",Skuld,"Kr" ) #
                print("---------------------------------------------------------------") #
    elif val == 4: #
        break #