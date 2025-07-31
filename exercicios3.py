# 1. Escrever um algoritmo que lê vários valores positivos e negativos (diferente
# de zero) e conte quantos destes valores são negativos e quantos são
# valores positivos, escrevendo estas informações. O algoritmo para quando
# você digitar zero.
#
# print("==================================================================")
# pos = 0
# neg = 0
# num = float(input("Insira um número: "))
# while num != 0:
#     if num > 0:
#         pos += 1
#         print(f"Tem {pos} numeros positivo e {neg} numeros negativos")
#         num = float(input("Insira outro número: "))
#
#     else:
#         neg += 1
#         print(f"Tem {pos} numeros positivo e {neg} numeros negativos")
#         num = float(input("Insira um número: "))
#
# print("Fim do programa")
# print("==================================================================")
#
#
# 2. Escreva um algoritmo que leia 20 valores positivos e encontre o maior e o
# menor deles. Mostre o resultado. Faça um contador de valores já digitados
# e enquanto menor que 20 obtenha dados. (posteriormente vamos utilizar
# o comando FOR para esses casos)
#
# print("==================================================================")
# num = int(input("Insita um valor positivo: "))
# maior = num
# menor = num
# tentativas = 19
# while tentativas > 0:
#     if num > 0:
#         print(f"Voce tem {tentativas} tentativas!")
#         num = int(input("Insita um valor positivo: "))
#         tentativas -= 1
#         if num > maior:
#             maior = num
#             print(f"O maior numero é {maior}, e o menor é {menor}")
#         elif num < menor:
#             menor = num
#             print(f"O maior numero é {maior}, e o menor é {menor}")
#
#     else:
#         print("Numero negativo invalido")
#         print("Fim do teste")
#         break
#
# print("==================================================================")
#
# 3. A prefeitura de uma cidade vez uma pesquisa entre seus habitantes,
# coletando dados sobre o salário e número de filhos. A prefeitura deseja
# saber, seu programa deve receber (digitado) o salário de cada pessoa e o
# número de filhos, para determinar:
# a) média do salário da população;
# b) média do número de filhos;
# c) maior salário
# d) percentual de pessoas com salário até R$100,00.
# O final da leitura de dados se dará com a entrada de um salário negativo.
#
# print("==================================================================")
# condicao = 1
# pesquisa = 1
# total_salario = 0
# total_filhos = 0
# salario = 0
# maior = 0
# while condicao >0:
#     print(f"Pesquisa numero {pesquisa}")
#     salario = float(input("Digite o salario: "))
#     filhos = int(input("Digite o numero de filhos: "))
#     if salario >= maior:
#         maior = salario
#     total_salario = total_salario + salario
#     total_filhos = total_filhos + filhos
#     print(f"O maior salario é de R${maior}, a media de salario é de R${total_salario/pesquisa} e a media de filhos é {total_filhos/pesquisa}")
#     condicao = int(input("Digite um valor maior q 0 para continuar: "))
#     pesquisa += 1
# print("Fim do programa")
# print("==================================================================")
#
#
# 4. Chico tem 1,50 metro e cresce 2 centímetros por ano, enquanto Zé tem
# 1,30 metro e cresce 3 centímetros por ano. Construa um algoritmo que
# calcule e imprima quantos anos serão necessários para que Zé seja maior
# que Chico.
# print("==================================================================")


# print("==================================================================")


# 5. Construir um algoritmo que calcule a média aritmética de vários valores
# inteiros positivos, digitados pelo usuário. O final da leitura acontecerá
# quando for lido um valor negativo.
# print("==================================================================")


# print("==================================================================")

# 6. Em uma eleição presidencial existem quatro candidatos. Os votos são
# informados através de códigos. Os dados utilizados para a contagem dos
# votos obedecem à seguinte codificação:
# 1,2,3,4 = voto para os respectivos candidatos;
# 5 = voto nulo;
# 6 = voto em branco.
# Elabore um algoritmo que leia o código do candidato em um voto. Calcule
# e escreva as seguintes informações:
# a) total de votos para cada candidato;
# b) total de votos nulos;
# c) total de votos em branco.
# Como finalizador do conjunto de votos, utilize o valor 0.
# print("==================================================================")


# print("==================================================================")

# 7. Escrever um algoritmo que leia uma variável n e calcule a tabuada de 1 até
# n. Mostre a tabuada na forma:
# 1 x n = n
# 2 x n = 2n
# 3 x n = 3n
# ...............
# n x n = n2
# print("==================================================================")


# print("==================================================================")

# 8. Escrever o algoritmo que leia os valores n1 e n2 e imprima o intervalo
# fechado (incluindo os limites) entre esses dois valores.

# print("==================================================================")


# print("==================================================================")

# 9. Escrever um algoritmo que leia um número n que indica quantos valores
# devem ser lidos a seguir. Para cada número lido, mostre o valor lido e o
# fatorial deste valor.


# print("==================================================================")


# print("==================================================================")

# 10. Escrever um algoritmo que leia um número não determinado de valores e
# calcule a média aritmética dos valores lidos, a quantidade de valores
# positivos, a quantidade de valores negativos e o percentual de valores
# negativos e positivos. Mostre os resultados.

# print("==================================================================")



# print("==================================================================")
# 11. Escrever um algoritmo que leia uma quantidade desconhecida de números
# e conte quantos deles estão nos seguintes intervalos: [0,25], [26,50],
# [51,75] e [76,100]. A entrada de dados deve terminar quando for lido um
# número negativo.

# print("==================================================================")



# print("==================================================================")
# 12. Faça um algoritmo que leia uma quantidade não determinada de números
# positivos. Calcule a quantidade de números pares e ímpares, a média de
# valores pares e a média geral dos números lidos. O número que encerrará
# a leitura será zero.


# print("==================================================================")



# print("==================================================================")
# 13. Uma empresa deseja aumentar seus preços em 20%. Faça um algoritmo
# que leia o código e o preço de custo de cada produto e calcule o preço
# novo. Calcule também, a média dos preços com e sem aumento. Mostre o
# código e o preço novo de cada produto e, no final, as médias. A entrada de
# dados deve terminar quando for lido um código de produto negativo.


# print("==================================================================")




# print("==================================================================")
# 14. Escreva um algoritmo que gere o números de 1000 a 1999 e escreva
# aqueles que divididos por 11 dão resto igual a 5.


# print("==================================================================")




# print("==================================================================")
# 15. Escreva um algoritmo que lê um valor n inteiro e positivo e que calcula a
# seguinte soma:
# S = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n
# O algoritmo deve escrever cada termo gerado e o valor final de S.


# print("==================================================================")



# print("==================================================================")
# 16. Escrever um algoritmo que lê 10 valores, um de cada vez, e conte quantos
# deles estão no intervalo [10,20] e quantos deles estão fora do intervalo,
# escrevendo estas informações.


# print("==================================================================")




# print("==================================================================")
# 17. Escrever um algoritmo que gere e escreva os 3 primeiros números
# perfeitos. Um número perfeito é aquele que é igual a soma dos seus
# divisores. (Ex.: 6 = 1+2+3; 28= 1+2+4+7+14, etc).



# print("==================================================================")



# print("==================================================================")
# 18. Escrever um algoritmo que leia um valor N inteiro e positivo e que calcula
# o valor de E. Imprime o resultado de E ao final.
# E = 1 + 1 / 1! + 1 / 2! + 1 / 3! + 1 / N!