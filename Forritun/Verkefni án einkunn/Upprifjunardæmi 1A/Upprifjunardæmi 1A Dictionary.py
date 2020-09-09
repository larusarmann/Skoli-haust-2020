#Liður 1
safn = {"A":"API","B":"banani","C":"cookies","D":"Diskur","E":"epli","F":"franskar","G":"gaur","H":"Hangikjt"}
#lidur2 
for k,v in safn.items():
    print(k, "er fyrir", v)
#lidur3
print(safn["E"])
#Lidur4
safn["H"]="hanastel"
#Lidur5
for k,v in safn.items()
    print(k,"er fyrir",v)
#liður 6
del safn["c"]
print("******safnð án c *******")
#liður 7
for k,v in safn.items()
    print(k, "er fyrir", v)
#liður 8
safn.popitem()
print("búið að henda út aftasta stakinu")
#liður 9
for k,v in safn.items():
    print(k,"er fyrir",v)
#Lidur10
safn2 = safn.copy
safn2["c"] ="Cookies"
print("afrit af safninu")
for k,v in safn2.items():
    print(k,"er fyrir",v)
print("hitt safnið")
for k,v in safn.items():
    print(k,"er fyrir",v)
#Lidur11
del safn2
#Lidur12
"""
ef  ég keyri þennan kóða fæ ég villu
for k,v in safn2.items():
    print(k,"er fyrir",v)
"""
#liður 13
import random
tolusafn={}
for x in range(1,6):
    tolusafn[x]=random.randint(100,1000)
print("tölusafn")
for k,v in tolusafn.items():
    print(k,"    ",v)
