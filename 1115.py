# https://www.urionlinejudge.com.br/judge/pt/problems/view/1115 
def quadrante():
    while True:
        x, y = [int(x) for x in input().split()]
        if x == 0 or y == 0:
            break
        elif x > 0 and y > 0:
            print("primeiro")
        elif x < 0 and y > 0:
            print("segundo")
        elif x < 0 and y < 0:
            print("terceiro")
        else:
            print("quarto")


quadrante()