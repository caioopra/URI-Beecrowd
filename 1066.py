valor_par = 0
valor_impar = 0
valores_positivos = 0
valores_negativos = 0

for i in range(5):
    entrada = int(input())
    
    if entrada % 2 == 0:
        valor_par += 1
    else:
        valor_impar += 1

    if entrada > 0:
        valores_positivos += 1
    elif entrada < 0:
        valores_negativos += 1

print("{} valor(es) par(es)".format(valor_par))
print("{} valor(es) impar(es)".format(valor_impar))
print("{} valor(es) positivo(s)".format(valores_positivos))
print("{} valor(es) negativo(s)".format(valores_negativos))
