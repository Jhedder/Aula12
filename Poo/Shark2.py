class Shark():
    def nadar(self):
        print("O tubarão está nadando.")

    def nadar_de_costas(self):
        print("O tubarão não consegue nadar para trás, mas pode afundar para trás.")

    def esqueleto(self):
        print("O esqueleto do tubarão é feito de cartilagem.")

class Clowfish():
    def nadar(self):
        print("O peixe palhaço está nadando.")
    
    def nadar_de_costas(self):
        print("O peixe palhaço pode nadar para trás.")

    def esqueleto(self):
        print("O esqueleto do Peixe Palhaço é feito de osso.")

shark = Shark()
shark.esqueleto()

clowfish = Clowfish()
clowfish.esqueleto()