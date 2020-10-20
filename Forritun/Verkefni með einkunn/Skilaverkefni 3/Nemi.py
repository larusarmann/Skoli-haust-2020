#Lárus Ármann Kjartansson
#19.10.2020
#Skilaverkefni 3

class Nemi():
    def __init__(self,kenn,nafn,kyn,postnumer,nafnSkola,email):
        self.kenn = kenn
        self.nafn = nafn
        self.kyn = kyn
        self.postnmr = postnumer
        self.nafnSkola = nafnSkola
        self.email = email
        
    def __str__(self):
        return self.nafn+" "+self.kenn+" "+self.nafnSkola
    # def __str__(self):
    #     return str(self.kenn,self.nafn,self.kyn,self.postnmr,self.nafnSkola,self.email)

class Grunnskolanemi(Nemi):
    def __init__(self,kenn,nafn,kyn,postnumer,nafnSkola,email,forrm):
        Nemi.__init__(self,kenn,nafn,kyn,postnumer,nafnSkola,email)
        self.forradamadur = forrm

    def __str__(self):
        return self.nafn+" "+self.kenn+" "+self.nafnSkola

class Framhaldsskolanemi(Nemi):
    def __init__(self,kenn,nafn,kyn,postnumer,nafnSkola,email,brHeiti,fjAfanga,busetus=False):
        Nemi.__init__(self,kenn,nafn,kyn,postnumer,nafnSkola,email)
        self.brHeiti=brHeiti
        self.fjAfanga=fjAfanga
        self.busetus=busetus
    def __str__(self):
        return self.nafn+" "+self.kenn+" "+self.nafnSkola
    def afangaUtskrift(self):
        return self.nafn+" "+str(self.fjAfanga)+" "+self.email
    def bondaUtskrift(self):
        return self.nafn+" "+str(self.postnmr)

class Haskolanemi(Nemi):
    def __init__(self,kenn,nafn,kyn,postnumer,nafnSkola,email,st,namsk,namslan=False):
        Nemi.__init__(self,kenn,nafn,kyn,postnumer,nafnSkola,email)
        self.stigNams = st
        self.namslan = namslan
        self.namslanSkuld = namsk
    
    def __str__(self):
        return self.nafn+" "+self.nafnSkola 
    
    def skuldUtskrift(self):
        return self.nafn+" "+str(self.namslanSkuld)+" Kr"
