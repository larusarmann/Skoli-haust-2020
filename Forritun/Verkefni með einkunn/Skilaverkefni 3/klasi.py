class Verkalydsfelag:
    def __init__(self,nafn,felagsnumer,laun,kennitala):
        self.nafn=nafn
        self.kennitala = kennitala
        self.felagsnumer = felagsnumer
        self.laun = laun

    def skatt(self):
        return int(self.laun)*0.36

    def utborgud_laun(self):
        pass

    def prenta_upplysingar_um_medlim(self):
        return self.felagsnumer.ljust(5)+"\t"+self.nafn.ljust(30)+"\t\t"+self.kennitala.ljust(13)+"\t\t"+self.laun
      