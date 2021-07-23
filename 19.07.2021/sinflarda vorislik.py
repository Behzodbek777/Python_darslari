# ajdod
class Nokia:
    def __init__(self, marka, yili, gaplashish, sms, kamera):
        self.marka = marka
        self.yili = yili
        self.gaplashish = gaplashish
        self.sms = sms
        self.kamera = kamera


# voris

class Samsung(Nokia):
    def yangilik(self, telegram, instagam, hdCamera):
        self.telegram = telegram
        self.instagram = instagam
        self.hdCamera = hdCamera


nokia6300 = Nokia("6300", 2000, True, True, True)
samsungJ2 = Samsung("Samsung J2", 2015, True, True, True)
samsungJ2.yangilik("bor", "bor", "bor")
print(nokia6300.__dict__)
print(samsungJ2.__dict__)
