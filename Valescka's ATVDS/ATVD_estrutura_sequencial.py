#1 - Faça um Programa que mostre a mensagem "Alo mundo" na tela.

print ("Alô mundo!")

#2 - Faça um Programa que peça um número e então mostre a mensagem.

numero = int (input("Insira um número, agradeço: "))
print (numero)

#3 - Faça um Programa que peça dois números e imprima a soma.

num1 = int (input("Um número, pfvr: "))
num2 = int (input("Oto número, pls: "))

soma = num1 + num2

print(soma)

#4 - Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = float (input("Insira a nota: " ))
nota2 = float (input("Insira a nota: " ))
nota3 = float (input("Insira a nota: " ))
nota4 = float (input("Insira a nota: " ))

media = (nota1 + nota2 + nota3 + nota4)/4

print ("A média é: " ,media)

#5 - Faça um Programa que converta metros para centímetros.

m = float (input("Diga uma medida em metros para que ela seja convertida para centímetros: " ))
print ("A medida convertida é igual a:", m*100)

#6 - Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

r = float (input("Insira o raio de um circulo: " ))
area = (3.14 * (r ** 2))
print(area)

#7 - Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

quadrado = float (input("Insira a medida do quadrado: "))
d_area = ((quadrado ** 2)*2)
print(d_area)

#8 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

hora = float (input("Quanto você ganha por hora? "))
horaMes = float (input("Quantas horas você trabalha por mês? "))
sMensal = hora * horaMes
print (f"O seu salário mensal é R$ {sMensal:,.2f}")

#9 - Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).

tFahrenheit = int(input("Digite uma temperatura em Fahrenheit: "))
tCelsius = 5*((tFahrenheit-32)/9)
print (f"A temperatura em Celsius é: {tCelsius:,.2f}")

#10 - Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

tCelsius2 = int(input("Digite uma temperatura em Celsius: "))
tFahrenheit2 = (1.8 * tCelsius2) + 32
print (f"A temperatura em Fahrenheit é: {tFahrenheit2:,.2f}")
