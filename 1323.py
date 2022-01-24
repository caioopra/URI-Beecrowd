entrada = 1
while entrada != 0:
    entrada = int(input())
    resultado = 0

    if entrada == 0:
        break

    for i in range(entrada, 0, -1):
        resultado += i ** 2
    print(resultado)