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


jiguli = Lada({"haydash":"mumkin"}, True, "bor", False, True)

lada_xRay_Cross = xRay(True, True, True, True, True)
lada_xRay_Cross.yangi(True, True, True)

print(jiguli.__dict__)
print(lada_xRay_Cross.__dict__)