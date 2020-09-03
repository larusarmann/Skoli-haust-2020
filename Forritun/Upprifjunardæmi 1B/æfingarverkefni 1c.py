

#Lidur A lesa og opna skra
with open("H:/Skóli/Forritun3/Upprifjunardæmi 1B/Skra.txt","w",encoding='utf=8') as f:
    for x in range(20):
        tala=pow(2,x)
        f.write(str(tala)+" ")
        #print(tala)
#Lidur B
listi=[] 
str_listi=[]
with open("H:/Skóli/Forritun3/Upprifjunardæmi 1B/Skra.txt","r",encoding='utf=8') as f:
    lina=f.read()
    lina.strip() # tek af endunum bil 
    str_listi=lina.split(" ")
    str_listi.remove((''))
    listi=list(map(str_listi))
print(listi)
teljari=0
for tala in listi:
    teljari+=1
    print(tala, end=" ")
    if teljari==10:
        print()#new line
#Lidur C
listi_an_6=[]
listi_6 =[]
for str_tala in str_listi:
    if str_tala[-1]="6":
        listi_6.append(int(str_tala))
    else:
        listi_an_6.append(int(str_tala))
#Listi med ollum tolum
print(listi_6)
print(listi_an_6)

    
