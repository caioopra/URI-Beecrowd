# https://www.urionlinejudge.com.br/judge/pt/problems/view/2057 
def calcular_fuso(saida, tempo, fuso):
    hora = saida + tempo + fuso
    
    if hora < 0:
        hora += 24
    elif hora == 24:
        hora = 0
    elif hora > 24:
        hora = hora - 24

    print(hora)

saida, tempo, fuso = [int(x) for x in input().split()]
calcular_fuso(saida, tempo, fuso)