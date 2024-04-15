class Animal:

   def __init__(self, nome, especie, sexo, cor, nomeCientifico, idade, origem):

       self.nome = nome

       self.especie = especie

       self.sexo = sexo

       self.cor = cor

       self.nomeCientifico = nomeCientifico

       self.idade = idade

       self.origem = origem


   def fazerSom(self):

       print(f"{self.nome} fez um som.")


   def andar(self, local):

       print(f"{self.nome} se moveu para {local}")


   def pular(self):

       print(f"{self.nome} se alimentou.")


a1 = Animal(nome = "Poseidon", especie = "Baiacu de agua doce", sexo = "Feminino", cor = "Amarelo", nomeCientifico = "Colomesus asellus", idade = "4 anos", origem = "Colombia")


print("Teste de baiacu:")

print(a1.nome)

print(a1.especie)

print(a1.sexo)

print(a1.cor)

print(a1.nomeCientifico)

print(a1.idade)

print(a1.origem)

print(" ")

class Cat(Animal):

   def __init__ (self, nome, especie, sexo, cor, nomeCientifico, idade, origem, patas):

       super().__init__(nome, especie, sexo, cor, nomeCientifico, idade, origem)

       self.patas = patas


   def arranhar(self, vitima):

       print(f"{self.nome} arranhou um(a) {vitima}")


   def mecherPatas(self, patas):

       print(f"{self.nome} mecheu {patas} patas.")


c1 = Cat(nome = "Austévio", especie = "Gato de rua", sexo = "Masculino", cor = "Branco e preto", nomeCientifico = "Felis silvestris catus", idade = "1 ano", origem = "Oriente Médio", patas = "4 patas")


print("Teste de gato:")

print(c1.nome)

print(c1.especie)

print(c1.sexo)

print(c1.cor)

print(c1.nomeCientifico)

print(c1.idade)

print(c1.origem)

print(c1.patas)
