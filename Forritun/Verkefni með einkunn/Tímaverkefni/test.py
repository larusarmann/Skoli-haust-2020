import random

spilin=["H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "H11", "H12", "H13", 
        "T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8", "T9", "T10", "T11", "T12", "T13", 
        "S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10", "S11", "S12", "S13", 
        "L1", "L2", "L3", "L4", "L5", "L6", "L7", "L8", "L9", "L10", "L11", "L12", "L13",]
notandi=[]
talva=[]

for x in range(25):
    randomspil=random.choice(spilin)
    notandi.append(randomspil)
print(notandi)
for x in range(25):
    randomspil=random.choice(spilin)
    talva.append(randomspil)
print(talva)