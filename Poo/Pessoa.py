#Exemplo de fazer uma lista de objetos
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return f"Pessoa(nome='{self.nome}', idade={self.idade})"
    
pessoa1 = Pessoa("alice",15)
pessoa2 = Pessoa("Pedro",20)
pessoa3 = Pessoa("Otavio",18)

lista_pessoas = [pessoa1, pessoa2, pessoa3]

for pessoa in lista_pessoas:
    print(f"Nome: {pessoa.nome} Idade: {pessoa.idade}")