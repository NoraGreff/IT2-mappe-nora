class Bruker :
    '''Superklasse for brukere i skole systemet. Skal ikke brukes direkte

    attributes:
        epost: en string med bruksers epost
        fornavn: en string med bruksers fornavn
        etternavn: en string med bruksers etternavn

    '''
    def __init__(self, epost, fornavn, etternavn) :
        self.epost = epost
        self.fornavn = fornavn
        self.etternavn = etternavn

    def logg_inn(self):
        print(f"{self.epost} logget inn")

    def logg_ut(self):
        print(f"{self.epost} logget ut")

class Lærer(Bruker) :
    def __init__(self,  epost, fornavn, etternavn,lønnskonto) :
        super().__init__(epost, fornavn, etternavn)
        self.lønnskonto = lønnskonto

ravi= Lærer("ravim@viken.no", "David Ravi", "Manikarnika", 970034056654)
ravi.logg_inn()

class Elev (Bruker):
    def __init__(self, trinn, klasse, fag, epost, fornavn, etternavn) :
        super().__init__(epost, fornavn, etternavn)
        self.trinn = trinn
        self.klasse = klasse
        self.fag = fag

if __name__ =="__main__":
    ravi = Lærer("ravim@viken.no", "David Ravi", "Manikarnika", 970034056654)


class Faglærer :
    def __init__(self, kompetanse, klasser) :
        self.kompetanse = kompetanse
        self.klasser = klasser

class Kontaktærer :
    def __init__(self, klasse, trinn) :
        self.klasse = klasse
        self.trinn = trinn
        
        


