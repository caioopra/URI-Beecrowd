# https://www.beecrowd.com.br/judge/pt/problems/view/1173?origem=1

lista = list(range(10))

entrada = 51
while entrada > 50:
    entrada = int(input())

lista[0] = entrada
print(f"N[0] = {lista[0]}")

for i in range(1, 10):
    lista[i] = lista[i - 1] * 2
    print(f"N[{i}] = {lista[i]}")
