class Mashina:
    def __init__(self, rusumi, narxi, chiqqan_yili):
        self.rusumi = rusumi
        self.narxi = narxi
        self.chiqqan_yili = chiqqan_yili

    def haqida(self):
        if self.narxi > 200000000:
            print("men juda qimmat mashinaman!")
        else:
            print("meni bir amallab sotib olsa bo'ladi")


x = Mashina("malibu", 320000000, 2021)
print(x.__dict__)
x.haqida()

y = Mashina("Nexia", 97000000, 2021)
print(y.__dict__)
y.haqida()
