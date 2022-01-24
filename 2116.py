#https://www.beecrowd.com.br/judge/pt/problems/view/2116
def encontrar_primo(n):
    for i in range(n, -1, -1):
        if n > 1:
            for j in range(2, int(i / 2) + 1):
                if (i % j) == 0:
                    break
            else:
                return i

    
num1, num2 = [int(x) for x in input().split()]
p1 = encontrar_primo(num1)
p2 = encontrar_primo(num2)

resultado = p1 * p2
print(resultado)
