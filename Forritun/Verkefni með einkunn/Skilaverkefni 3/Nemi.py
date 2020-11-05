#Lárus Ármann Kjartansson
#19.10.2020
#Skilaverkefni 3

class Nemi():#Býr til Klasan
    def __init__(self,kenn,nafn,kyn,postnumer,nafnSkola,email): #býr til fall sem tekur inn nafn, postnmr, skolanafn og email
        self.kenn = kenn #upphafsstillir breytu klasans
        self.nafn = nafn #upphafsstillir breytu klasans
        self.kyn = kyn #upphafsstillir breytu klasans
        self.postnmr = postnumer #upphafsstillir breytu klasans
        self.nafnSkola = nafnSkola #upphafsstillir breytu klasans
        self.email = email #upphafsstillir breytu klasans
        
    def __str__(self): #býr til fall
        return self.nafn+" "+self.kenn+" "+self.nafnSkola #segir hvað á að prentast og hvernig

class Grunnskolanemi(Nemi): #Býr til Klasan
    def __init__(self,kenn,nafn,kyn,postnumer,nafnSkola,email,forradamadur): #býr til fall sem tekur inn nafn, postnmr, skolanafn, email og forráðamann
        Nemi.__init__(self,kenn,nafn,kyn,postnumer,nafnSkola,email) #býr til fall sem erfir frá "Nemi" aðalfallinu
        self.forradamadur = forradamadur #

    def __str__(self): #býr til fall
        return self.nafn+" "+self.kenn+" "+self.nafnSkola #segir hvað á að prentast og hvernig

class Framhaldsskolanemi(Nemi): #Býr til Klasan
    def __init__(self,kenn,nafn,kyn,postnumer,nafnSkola,email,brautarHeiti,fjoldiAfanga,busetustyrkur=False): #býr til fall sem tekur inn nafn, postnmr, skolanafn, email, brautarheiti, fjolda afanga og búsetustyrk
        Nemi.__init__(self,kenn,nafn,kyn,postnumer,nafnSkola,email) #býr til fall sem erfir frá "Nemi" aðalfallinu
        self.brautarHeiti=brautarHeiti #upphafsstillir breytu klasans
        self.fjoldiAfanga=fjoldiAfanga #upphafsstillir breytu klasans
        self.busetustyrkur=busetustyrkur #upphafsstillir breytu klasans
    def __str__(self): #býr til fall
        return self.nafn+" "+self.kenn+" "+self.nafnSkola #segir hvað á að prentast og hvernig
    def afangaUtskrift(self): #býr til fall
        return self.nafn+" "+str(self.fjoldiAfanga)+" "+self.email #segir hvað á að prentast og hvernig
    def bondaUtskrift(self): #býr til fall
        return self.nafn+" "+str(self.postnmr) #segir hvað á að prentast og hvernig

class Haskolanemi(Nemi): #Býr til Klasan
    def __init__(self,kenn,nafn,kyn,postnumer,nafnSkola,email,stigNams,namslanSkuld, namslan=False): #býr til fall sem tekur inn allt
        Nemi.__init__(self,kenn,nafn,kyn,postnumer,nafnSkola,email) #býr til fall sem erfir frá "Nemi" aðalfallinu
        self.stigNams = stigNams #upphafsstillir breytu klasans
        self.namslan = namslan #upphafsstillir breytu klasans
        self.namslanSkuld = namslanSkuld #upphafsstillir breytu klasans
    
    def __str__(self): #býr til fall
        return self.nafn+" "+self.nafnSkola #segir hvað á að prentast og hvernig
    
    def skuldUtskrift(self): #býr til fall
        return self.nafn+" "+str(self.namslanSkuld)+" Kr" #segir hvað á að prentast og hvernig
