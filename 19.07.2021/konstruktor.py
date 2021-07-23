""" konstruktorlar """
class Komputer():
    komp1 = "Lenovo"

print(Komputer.komp1)

# parametrli

class Komputer1():
    def __init__(self, Firma, HDD, RAM, SSD, VideoCard, Prossesor):
        self.Firma = Firma
        self.HDD = HDD
        self.RAM = RAM
        self.SSD = SSD
        self.VideoCard = VideoCard
        self.Prossesor = Prossesor


komp1 = Komputer1("lenovo", "500 Gb", 4, "", "Nvidia geFose 4Gb 10200", "Core i-7 10500h")
print(komp1.__dict__)
komp2 = Komputer1("Dell", 1, 4, 120,"", "core i-5")
print(komp2.__dict__)