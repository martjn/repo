class Song(object):

    def __init__(self, sõna):
        self.sõnad = sõna

    def laula_mu_laulu(self):
        for rida in self.sõnad:
            print(rida)
    

laul1 = Song(["Mu isamaa,", "Mu õnn ja rõõm", "Kui kaunis oled sa"])
laul2 = Song(["Sa oled mind,", "ju sünnitand", "ja üles kasvatand"])

laul1.laula_mu_laulu()

laul2.laula_mu_laulu()
