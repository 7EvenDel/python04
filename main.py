class City():
    def __init__(self, name):
        self.name = name
    def info(self):
        pass

class Strasbourg(City):
    pass
class Toulouse(City):
    pass
class Marseille(City):
    pass
class Birmingham(City):
    pass
class Manchester(City):
    pass
class Canberra(City):
    pass
class Sydney(City):
    pass
class Melbourne(City):
    pass

# Types:
class Australia(Sydney, Melbourne, Canberra):  
    def info(self):
        print(f"{self.name} city Australia")

class France(Marseille, Toulouse, Strasbourg):   
    def info(self):
        print(f"{self.name} city France")

class GreatBritian(Birmingham, Manchester):   
    def info(self):
        print(f"{self.name} city Great Britian")
    
class Europa(France, GreatBritian):
    def info(self):
      print(f"{self.name} city Europa")

strasbourg = France("strasbourg")
toulouse = France("toulouse")
marseille = France("marseille")
birmingham = GreatBritian("birmingham")
manchester = GreatBritian("manchester")
canberra =  Australia("canberra")
sydney = Australia("sydney")
melbourne = Australia("melbourne")

marseille.info()
sydney.info()
birmingham.info()