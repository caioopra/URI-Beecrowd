nome = input()
salarioFixo = float(input())
vendas = float(input())

salarioFinal = salarioFixo + 0.15 * vendas

print("TOTAL = R$ {:.2f}".format(salarioFinal))