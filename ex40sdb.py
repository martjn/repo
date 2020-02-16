class multiplier(object):

    def __init__(self, arvud):
        self.arvud = arvud

    def korrutaja(self):
        lisa = []
        for arv in self.arvud:
            arv *= 9
            lisa.append(arv)
        print(lisa)

    def korrutaja2(self):
        for arv in self.arvud:
            while len(self.arvud) < 40:
                self.arvud.append(arv*3)
                print(self.arvud)
        print(self.arvud)


valem = multiplier([1, 97, 23, 656])
valem2 = multiplier([3, 345, 123, 456])
valem.korrutaja()
valem2.korrutaja()

