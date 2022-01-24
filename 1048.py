# https://www.beecrowd.com.br/judge/pt/problems/view/1048
def calcular_aumento(salario):
    
    if salario <= 400:
        novo_salario = salario * 1.15
        reajuste = salario * 0.15
        percentual = 15
    elif salario <= 800:
        novo_salario = salario * 1.12
        reajuste = salario * 0.12
        percentual = 12
    elif salario <= 1200:
        novo_salario = salario * 1.1
        reajuste = salario * 0.1
        percentual = 10
    elif salario <= 2000:
        novo_salario = salario * 1.07
        reajuste = salario * 0.07
        percentual = 7
    else:
        novo_salario = salario * 1.04
        reajuste = salario * 0.04
        percentual = 4
    
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {percentual} %")


entrada = float(input())
calcular_aumento(entrada)