#1 - Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.


nota = float(input("digite a nota do aluno: "))
while nota <0 or nota >10:
  print ("Nota inválida")
  nota = float(input("digite a nota do aluno: "))

#2 - Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

nomeUsuario = input ("digite o nome do usuario: ")
senhaUsuario = input ("digite a sua senha: ")

while nomeUsuario == senhaUsuario:
  print ("ação não permitida, escolha uma senha diferente do nome")
  nomeUsuario = input ("digite o nome do usuario: ")
  senhaUsuario = input ("digite a sua senha: ")


#3 - Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.

for i in range (1,21):
  print (i)

print (" ")

for i in range (1,21):
  print (i, end= " ")

#4 - Faça um programa que leia 5 números e informe o maior número.

x=0
for i in range (1,6):
  num = int(input("digite um numero: "))
  if num > x:
    x=num

print(x)


#5 - Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = 0

for i in range (1,6):
  num = int(input("digite um numero: "))
  soma = soma + num

print ("A média dos números digitados é",soma/5)

#6 - Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

for i in range (1, 50):




#7 - Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
Altere o programa anterior para mostrar no final a soma dos números.

A = int(input("digite um numero: "))
B = int(input("digite um numero: "))
soma=0

for i in range ((A + 1), B):
  print (i)
  soma=soma+i

print(soma)

#8 - Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

numero = int(input("digite o número que você deseja ver a tabuada: "))

for i in range (1,11):
  print (numero, "X", i, "=", numero * i)
