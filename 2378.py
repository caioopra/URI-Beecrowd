# https://www.beecrowd.com.br/judge/pt/problems/view/2378
def sensor_elevador(leituras, capacidade):
    excedeu = 'N'
    passageiros = 0    

    for i in range(leituras):
        sairam, entraram = [int(x) for x in input().split()]

        passageiros = passageiros + entraram - sairam

        if passageiros > capacidade:
            excedeu = 'S'
    
    print(excedeu)


n, c = [int(x) for x in input().split()]
sensor_elevador(n, c)