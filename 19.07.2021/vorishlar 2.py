class Lada:
    def __init__(self, haydash, oyna_artgich, isitish_tizimi, sovutish_tizimi, musiqa):
        self.haydash = haydash
        self.oyna_artgich = oyna_artgich
        self.isitish_tizimi = isitish_tizimi
        self.sovutish_tizimi = sovutish_tizimi
        self.musiqa = musiqa


class xRay(Lada):
    def yangi(self, kruis_kontrol, pult, monitor):
        self.kruis_kontrol = kruis_kontrol
        self.pult = pult
        self.monitor = monitor

class Volga(Lada):
    pass

# xulosa. bitta classdan istalgancha voris olish mumkin

class Ota:
    def __init__(self,x):
        self.x = x

class Ona:
    def __init__(self,y):
        self.y = y


class Bola(Ota, Ona):
    pass
bola = Bola(5)
print(bola.x)