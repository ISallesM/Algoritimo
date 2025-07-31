
# print("=============================================================")
# print("Exercicios")
# print("1. Efetuar a leitura de uma nota e, se o valor for maior ou igual a 60, imprimir na tela 'APROVADO'.")
# nota = float(input("Qual valor da nota:"))
# if nota >= 60:
#     print("APROVADO")
# print("=============================================================")


# print("=============================================================")
# print("Exercicios")
# print("2. Efetuar a leitura de uma nota e, se o valor for maior ou igual a 60, imprimir na tela 'APROVADO', se for menor, imprimir reprovado.")
# nota = float(input("Qual valor da nota:"))
# if nota >= 60:
#     print("APROVADO")
# else:
#     print("REPROVADO")
# print("=============================================================")


# print("=============================================================")
# print("Exercicios")
# print("3. Efetuar a leitura de uma nota e, se o valor for maior ou igual a 60, imprimir na tela 'APROVADO', se for menor, imprimir reprovado. Testar ainda se o valor lido foi maior do que 100 ou menor do que zero. Neste caso, imprimir 'NOTA INVÁLIDA'.")
# nota = float(input("Qual valor da nota:"))
# if nota >= 0 and nota <=100:
#     if nota >= 60:
#         print("APROVADO")
#     else:
#         print("REPROVADO")
# else:
#     print("NOTA INVALIDA")
# print("=============================================================")


# print("=============================================================")
# print("Exercicios")
# print("4. Ler um número inteiro e informar se o número lido é par ou impar.")
# num = int(input("Qual valor da nota:"))
# val1 = num % 2
# if val1 ==0:
#     print("Numero Par")
# else:
#     print("Numero Impar")
# print("=============================================================")


# print("=============================================================")
# print("Exercicios")
# print("5. Ler um número inteiro e testar se o valor lido termina com 0 (divisível por 10). Em caso positivo, exiba a metade deste número. Caso contrário, exibir a mensagem 'O número digitado não termina com 0'.")
# num = int(input("Qual valor da nota:"))
# val1 = num % 10
# if val1 ==0:
#     print(num/2)
# else:
#     print("O número digitado não termina com 0")
# print("=============================================================")


# print("=============================================================")
# print("Exercicios")
# print("6. Ler um número e informar se ele é positivo, negativo ou neutro (zero).")
# num = int(input("Qual valor da nota:"))

# if num !=0:
#     if num > 0:
#         print("Positivo") 
#     else:
#         print("Negativo")
# else:
#     print("Neutro")
# print("=============================================================")



# print("=============================================================")
# print("Exercicios")
# print("7. Faça a leitura do salário atual e do tempo de serviço de um funcionário. A seguir, calcule o seu salário reajustado. Funcionários com até 1 ano de empresa, receberã o aumento de 10%. Funcionários com mais de um ano de tempo de serviço, receberã o aumento de 20%.")
# salario_atual = float(input("Qual salario atual:"))
# tempo_empresa = int(input("Quantos meses trabalha na empresa"))

# if tempo_empresa >12:
#     print(f"salario atual é de: R${salario_atual}, e com reajuste de 20% passa a ser de: R${salario_atual*(1+0.2)} por ter mais de um ano de empresa") 
    
# else:
#     print(f"salario atual é de: R${salario_atual}, e com reajuste de 10% passa a ser de: R${salario_atual*(1+0.1)} por ter menos de um ano de empresa") 
# print("=============================================================")



# print("=============================================================")
# print("Exercicios")
# print("8. Faça a leitura do ano atual e do ano de nascimento de uma pessoa e exibir sua idade. A seguir, informe se a pessoa é bebê (0 a 3 anos), criança (4 a 11 anos), adolescente (12 a 17 anos), adulta (18 a 64 anos) ou idosa (65 anos em diante).")
# ano = int(input("Em q ano estamos :"))
# nascimento = int(input("Em que ano vc nasceu :"))
# idade = ano - nascimento
# if idade < 4:
#     print(f"Essa pessoa tem {idade} anos e é bebê")
# elif idade < 12:
#     print(f"Essa pessoa tem {idade} anos e é criança")
# elif idade < 17:
#     print(f"Essa pessoa tem {idade} anos e é Adolescente")
# elif idade < 65:
#     print(f"Essa pessoa tem {idade} anos e é Adulta")   
# else:
#     print(f"Essa pessoa tem {idade} anos e é Idosa")
# print("=============================================================")



# print("=============================================================")
# print("Exercicios")
# print("9. Informar o número do mês do ano e mostrar o nome do mês por extenso. Caso o número do mês não exista, exibir a mensagem 'Mês inválido'.")
# mes = int(input("Digite o numero do mes atual :"))

# if mes == 1:
#     print("Janeiro")
# elif mes == 2:
#     print("Fevereiro")
# elif mes == 3:
#     print("Marco")
# elif mes == 4:
#     print("Abril") 
# elif mes == 5:
#     print("Maio")
# elif mes == 6:
#     print("Junho")
# elif mes == 7:
#     print("Julho")   
# elif mes == 8:
#     print("Agosto")
# elif mes == 9:
#     print("Setembro") 
# elif mes == 10:
#     print("Outubro")
# elif mes == 11:
#     print("Novembro")
# elif mes == 12:
#     print("Dezembro")   
# else:
#     print("Mês inválido")
# print("=============================================================")




# print("=============================================================")
# print("Exercicios")
# print("10. Faça um algoritmo que receba o valor do salário de uma pessoa e o valor de um financiamento pretendido. Caso o financiamento seja menor ou igual a 5 vezes o salário da pessoa, o algoritmo deverá escrever 'Financiamento Concedido'; senão, ele deverá escrever 'Financiamento Negado'.")
# salario_atual = float(input("Qual salario atual: "))
# valor_financiamento = float(input("Qual o valor do financiamento: "))
# condicao = salario_atual/valor_financiamento

# if condicao >= 5:
#     print("Financiamento Concedido")    
# else:
#     print("Financiamento Negado") 
# print("=============================================================")





# print("=============================================================")
# print("Exercicios")
# print("11. Escreva um programa para calcular e mostrar o salário semanal de uma pessoa, determinado pelas condições que seguem. Se o número de horas trabalhadas for inferior ou igual a 40, a pessoa recebe R$15,00 por hora, senão a pessoa recebe R$600,00 mais R$21,00 para cada hora trabalhada acima de 40 horas. O programa deve pedir o número de horas trabalhadas como entrada e deve dar o salário como saída.")
# horas_trabalhadas = int(input("Quantas horas foram trabalhadas: "))


# if horas_trabalhadas <= 40:
#     print(f"O salario é de R${horas_trabalhadas * 15}")    
# else:
#     print(f"O salario é de R${600 + (horas_trabalhadas -40) * 21 }")
# print("=============================================================")






#12. A taxa de juros aplicada em fundos depositados em um banco é
# determinada pelo tempo em que estes ficam depositados. Para um banco
# em particular, a seguinte tabela é usada:
# Tempo em depósito                                Taxa de juro
# Maior ou igual a 5 anos                              0,95
# Menor que 5 anos mas maior ou igual a 4 anos         0,90
# Menor que 4 anos mas maior ou igual a 3 anos         0,85
# Menor que 3 anos mas maior ou igual a 2 anos         0,75
# Menor que 2 anos mas maior ou igual a 1 ano          0,65
# Menor que 1 ano                                      0,55
# Usando esta informação, escreva um programa que receba o tempo em
# que os fundos foram mantidos em depósito e informe a taxa de juros
# correspondente.


# print("=============================================================")
# print("Exercicios")
# deposito = int(input("A quanto tempo mantem os seus fundos? :"))

# if deposito < 12:
#     print(f"Voce mantem um fundo a {deposito} meses, e sua taxa de juros corresponde a 0,55")  
# elif deposito < 24:
#     print(f"Voce mantem um fundo a {deposito} meses, e sua taxa de juros corresponde a 0,65")  
# elif deposito < 36:
#     print(f"Voce mantem um fundo a {deposito} meses, e sua taxa de juros corresponde a 0,75")  
# elif deposito < 48:
#     print(f"Voce mantem um fundo a {deposito} meses, e sua taxa de juros corresponde a 0,85")  
# elif deposito < 60:
#     print(f"Voce mantem um fundo a {deposito} meses, e sua taxa de juros corresponde a 0,90")  
# else:
#     print(f"Voce mantem um fundo a {deposito} meses, e sua taxa de juros corresponde a 0,95")  
# print("=============================================================")







# 13. Baseado no ano e peso do modelo de um automóvel, o estado de Nova
# Jersey determina a sua classe de peso e taxa de registro usando a seguinte
# tabela:
# Ano do modelo          Peso                                  Classe    Taxa de registro
# 1970 ou antes          Menos de 1200 kg                         1          16,50
#                        de 1200 a 1700 kg                        2          25,50
#                        Mais de 1700 kg                          3          46,50
# 1971 a 1979            Menos de 1200 kg                         4          27,00
#                        de 1200 a 1700 kg                        5          30,50
#                        Mais de 1700 kg                          6          52,50
# 1980 ou depois         Menos de 1600 kg                         7          19,50
#                        1600 kg ou mais                          8          55,50
# Usando esta informação, escreva um programa que receba o ano e o peso
# do modelo de um automóvel e calcule e imprima a classe de peso e a taxa
# de registro para o carro.

# print("=============================================================")
# print("Exercicios")
# ano = int(input("Qual o ano do automovel? :"))
# peso = int(input("Qual o peso do automovel? :"))

# if ano <= 1970:
#     if peso < 1200:
#         print(f"O automovel esta na classe 1, e sua taxa de registro corresponde a 16,50")  
#     elif peso < 1700:
#        print(f"O automovel esta na classe 2, e sua taxa de registro corresponde a 25,50") 
#     else:
#        print(f"O automovel esta na classe 3, e sua taxa de registro corresponde a 46,50")     
# elif ano < 1979:
#     if peso < 1200:
#        print(f"O automovel esta na classe 4, e sua taxa de registro corresponde a 27,00") 
#     elif peso < 1700:
#        print(f"O automovel esta na classe 5, e sua taxa de registro corresponde a 30,50") 
#     else:
#        print(f"O automovel esta na classe 6, e sua taxa de registro corresponde a 52,50") 
 
# else:
#     if peso < 1600:
#        print(f"O automovel esta na classe 7, e sua taxa de registro corresponde a 19,50") 
#     else:
#        print(f"O automovel esta na classe 8, e sua taxa de registro corresponde a 55,50") 
# print("=============================================================")





# 14. Desenvolva um algoritmo que leia o nome de um aluno, suas notas em 2
# provas e em um trabalho (todas com valores entre 0 e 10) e sua frequê ncia,
# definindo e imprimindo se ele foi aprovado, reprovado ou se fará prova final.
# O aluno será reprovado se faltou mais de 15 aulas. Será aprovado se nã o
# for reprovado por falta e sua mé dia for maior que 6,0. Caso tenha mé dia
# menor, deverá fazer prova final. O cá lculo da mé dia deve ser feito com peso
# 3 para a primeira prova, 5 para a segunda prova e 2 para o trabalho.


# print("=============================================================")
# nome = str(input("Nome aluno: "))
# prova1 = float(input("Valor da prova 1: "))
# prova2 = float(input("Valor da prova 2: "))
# trabalho = float(input("Valor do trabalho: "))
# faltas = int(input("Quantas faltas teve: "))
# media = ((prova1*3)+(prova2*5)+(trabalho*2))/10

# if (prova1 >= 0 and prova1 <= 10) and (prova2 >= 0 and prova2 <= 10) and (trabalho >= 0 and trabalho <= 10):
#     if faltas <= 15:
#         if media >= 6:
#             print(f"{nome} está Aprovado")
#         else:
#             print(f"{nome} está de Recuperação")
#     else:
#         print(f"{nome} está Reprovado por falta")    
# else:
#     print("Nota inválida")   
# print("=============================================================")





# 15. Faç a um algoritmo para verificar e imprimir entre 4 nú meros lidos qual é o
# menor.
# print("=============================================================")

# num1 = float(input("Digite o primeiro número: "))
# num2 = float(input("Digite o segundo número: "))
# num3 = float(input("Digite o terceiro número: "))
# num4 = float(input("Digite o quarto número: "))
# menor = num1

# if num2 < menor:
#     menor = num2
# if num3 < menor:
#     menor = num3
# if num4 < menor:
#     menor = num4
# print(f"O menor número entre os digitados é: {menor}")

# # Usando a função min() para encontrar o menor número
# ## Usando a função max() para encontrar o maior número

# menor = min(num1, num2, num3, num4)
# print(f"O menor número entre os digitados é: {menor}")
# # print("=============================================================")




# 16. Desenvolva um algoritmo que pergunte um código e de acordo com o valor
# digitado seja apresentado o cargo correspondente. Caso o usuário digite
# um código que não esteja na tabela, mostrar uma mensagem de código
# inválido. Utilize a tabela abaixo:
# Código   Cargo
# 101     Vendedor
# 102     Atendente
# 103     Auxiliar Técnico
# 104     Assistente
# 105     Coordenador de Grupo
# 106     Gerente
# # print("=============================================================")
# codigo = int(input("Digite o codigo: " ))

# if codigo == 101:
#     print("Vendedor")
# elif codigo == 102:
#     print("Atendente")
# elif codigo == 103:
#     print("Auxiliar Técnico")
# elif codigo == 104:
#     print("Assistente")
# elif codigo == 105:
#     print("Coordenador de Grupo")
# elif codigo == 106:
#     print("Gerente")
# else:
#     print("código inválido")
# # print("=============================================================")


#17. Uma encomenda de unidades de disco contém unidades marcadas com
#um código de 1 a 4, que indica o tipo seguinte:
#Código     Tipo da unidade
#1           CD-ROM (700MB)
#2           DVD-ROM (4.7GB)
#3           DVD-9 (8.54 GB)
#4           Blu-Ray (25 GB)
#Escreva um programa que receba o número de um código como entrada
#e, baseado no valor digitado, informe o tipo correto de unidade de disco.
# # print("=============================================================")

#codigo = int(input("Insira o numero do codigo: "))
#if codigo == 1:
#    print("CD-ROM (700MB)")
#elif codigo == 2:
#    print("DVD-ROM (4.7GB)")
#elif codigo == 3:
#    print("DVD-9 (8.54GB)")
#elif codigo == 4:
#    print("Blu-Ray (25 GB)")
#else:
#    print("Codigo invalido")

#18. Escreva um programa que receba dois números reais e um código de
#seleção do usuário. Se o código digitado for 1, faça o programa adicionar
#os dois números previamente digitados e mostrar o resultado; se o código
#de seleção for 2, os números devem ser multiplicados; se o código de
#seleção for 3, o primeiro número deve ser dividido pelo segundo. Se
#nenhuma das opções acima for escolhida, mostrar "Código inválido".
# # print("=============================================================")
#num1 = int(input("Digite o primeiro numero: "))
#num2 = int(input("Digite o segundo numero: "))
#codigo = int(input("Digite o Codigo: "))
#adicao = num1 + num2
#mult = num1 * num2
#div = num1 / num2
#if codigo == 1:
#    print(f"A primeira escolha é: {num1}. A segunda escolha é : {num2}. A suma é:  {adicao}")
#elif codigo == 2:
#    print(f"A primeira escolha é: {num1}. A segunda escolha é : {num2}. A suma é:  {mult}")
#elif codigo == 3:
#    print(f"A primeira escolha é: {num1}. A segunda escolha é : {num2}. A suma é:  {div}")
#else:
#    print("Codigo invalido")
# # print("=============================================================")


#19. Faça um algoritmo que transforme a nota de um aluno em conceito. As
#notas 10 e 9 receberão conceito A, as notas 8 e 7 receberão conceito B, as
#notas 6 e 5 receberão conceito C e abaixo de 5 conceito D.

# # print("=============================================================")
#nota = float(input("Insira a nota: "))
#if nota >= 0 and nota <= 10:
#    if nota >= 9:
#        print("Voce tirou um A")
#    elif nota >= 7:
#        print("Voce tirou um B")
#    elif nota >= 5:
#        print("Voce tirou um C")
#    elif nota < 5:
#        print("Voce tirou um D")
#else:
#    print("Nota invalida")

# # print("=============================================================")
#20. Desenvolva um algoritmo para que, dados dois valores inteiros entre 1 e
#10 lidos, calcule e imprima: a média dos números caso a soma deles for
#menor que 8, seu produto caso a soma seja igual a 8 ou a divisão do maior
#pelo menor caso a soma dos valores for maior que 8.

# # print("=============================================================")
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
soma = num1 + num2
media = soma/2
produto = num1 * num2
maior = num1
menor = num2

if num2 > num1:
    maior = num2
    menor = num1
if 1 <= num1 <= 10 and 1 <= num2 <= 10:
    if soma < 8:
        print(media)
    elif soma == 8:
        print(produto)
    else:
        print(maior/menor)
else:
    print("Codigo invalido")


# # print("=============================================================")