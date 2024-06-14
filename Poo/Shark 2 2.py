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

def polimorfismo_peixe(peixe):
    peixe.nadar()
    peixe.nadar_de_costas()
    peixe.esqueleto()

shark = Shark()
clowfish = Clowfish()

polimorfismo_peixe(shark)
polimorfismo_peixe(clowfish)

for peixe in (shark, clowfish):
    peixe.nadar()
    peixe.nadar_de_costas()
    peixe.esqueleto()
