# Lista de Exercícios – Entrada e Saída
# Desenvolver algoritmos para os problemas abaixo:
# 1. Efetuar a soma dos nú meros 5 e 10 e imprimir o resultado.
# 2. Efetuar a soma de trê s nú meros digitados pelo usuá rio e imprimir o resultado.
# 3. Efetuar a multiplicaç ã o de dois nú meros digitados pelo usuá rio e imprimir o resultado.
# 4. Calcular o aumento que será dado a um funcioná rio, obtendo do usuá rio as seguintes
# informaç õ es: salá rio atual e a porcentagem de aumento. Apresentar o novo valor do
# salá rio e o valor do aumento.
# 5. Converter uma quantidade de horas digitadas pelo usuá rio em minutos. Informe o
# resultado em minutos.
# 6. Calcular o salá rio lí quido do funcioná rio sabendo que este é constituí do pelo salá rio
# bruto mais o valor das horas extras subtraindo 8% de INSS do total. Serã o lidos nesse
# problema o salá rio bruto, o valor das horas extras e o número de horas extras.
# Apresentar ao final o salá rio lí quido.
# 7. Efetuar a leitura do nú mero de quilowatts consumidos e calcular o valor a ser pago
# de energia elé trica, sabendo-se que o valor a pagar por quilowatt é de 0,12.
# Apresentar o valor total a ser pago pelo usuá rio acrescido de 18% de ICMS.
# 8. Calcular a mé dia de combustí vel gasto pelo usuá rio, sendo informado a quantidade
# de quilô metros rodados e a quantidade de combustível consumidos

# print("=============================================================")
# print("Exercicios")
# print("1. Efetuar a soma dos numeros 5 e 10 e imprimir o resultado.")
# print("A soma de 5 + 10 é igual a :" , 5 + 10)
# print("=============================================================")


# print("=============================================================")
# print("2. Efetuar a soma de três numeros digitados pelo usuário e imprimir o resultado.")
# val1 = float(input("Insira o primeiro valor: "))
# val2 = float(input("Insira o segundo valor: "))
# val3 = float(input("Insira o terceiro valor: "))
# soma = val1+val2+val3
# print("A soma dos tres numeros sao: ",soma)
# print("=============================================================")



# print("================================================================")
# print("3. Efetuar a multiplicação de dois números digitados pelo usuário e imprimir o resultado.")
# val1 = float(input("insira o primeiro numero"))
# val2 = float(input("insira o segundo numero"))
# multiplicacao = val1 * val2
# print("O valor da multiplicaçao dos numeros é : " ,multiplicacao)
# print("=============================================================")


print("=============================================================")
print(" 4. Calcular o aumento que será dado a um funcionário, obtendo do usuário as seguintes informações: salário atual e a porcentagem de aumento. Apresentar o novo valor do salário e o valor do aumento.")
salario = float(input("Insira o valor do Salario:"))
aumento = float(input("Insira o percentual do aumento:"))
novo_salario = (salario * (aumento/100))
print(f"O salario atual é de: R${salario} e terá um aumento de {aumento}%, com isso o novo salario sera num valor de : R${novo_salario}")
print("=============================================================")

# print("=============================================================")
# print("5. Converter uma quantidade de horas digitadas pelo usuário em minutos. Informe o resultado em minutos.")
# horas = int(input("Insira a quantidade de horas:"))
# conversao = horas* 60
# print(f"{horas} horas é o mesmo que {conversao} minutos")
# print("=============================================================")

# print("=============================================================")
# print("6. Calcular o salário líquido do funcionário sabendo que este é constituído pelo salário bruto mais o valor das horas extras subtraindo 8% de INSS do total. Serão lidos nesse problema o salário bruto, o valor das horas extras e o número de horas extras. Apresentar ao final o salário líquido.")
# salario_bruto = float(input("Salario bruto: "))
# val_horas_extras = int(input("Insita o valor de cada hora extra"))
# quantidade_horas_trabalhadas = float(input("quantas horas extras forasm trabalhadas: "))
# salario_liquido = ((salario_bruto + (val_horas_extras * quantidade_horas_trabalhadas)) * 92/100) 
# print(f"o valor do salario bruto é de: R${salario_bruto}")
# print(f"o valor de cada hora extra é de: R${val_horas_extras}")
# print(f"A quantidade de horas extras foi de :{quantidade_horas_trabalhadas}")
# print(f"Com isso o valor liquido recebido sera de: R${salario_liquido}")
# print("=============================================================")

# print("=============================================================")
# print("7. Efetuar a leitura do número de quilowatts consumidos e calcular o valor a ser pago de energia elétrica, sabendo-se que o valor a pagar por quilowatt é de 0,12. Apresentar o valor total a ser pago pelo usuário acrescido de 18% de ICMS.")
# kwh = float(input("QTOS KW/H foi consumido:"))
# imposto = (1 + 18/100)
# valor = float(kwh * 0.12)
# valor_total = valor * imposto 
# print(f"O consumo foi de {kwh:.2f}kw/h, e o valor a se pagar é de: R${valor_total:.2f}. Ja com um imposto de 18%")
# print("=============================================================")

# print("=============================================================")
# print("8. Calcular a média de combustível gasto pelo usuário, sendo informado a quantidade de quilômetros rodados e a quantidade de combustível consumidos")
# km = float(input("qtos kms forams rodados"))
# litros = float(input("qtos litros foram usados"))
# consumo = km/litros
# print(f"A media de consumo desse veiculo é de: {consumo} km/l")
# print("=============================================================")
