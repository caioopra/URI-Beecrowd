horas = int(input())
velMedia = int(input())

quilometros = horas * velMedia
consumo = quilometros / 12

print("{:.3f}".format(consumo))