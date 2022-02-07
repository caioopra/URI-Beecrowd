# https://www.beecrowd.com.br/judge/pt/problems/view/1953?origem=1
while True:
    try: 
        N = int(input())

        alunos = {
            "EPR": 0,
            "EHD": 0,
            "INTRUSOS": 0
        }

        for i in range(N):
            matricula, curso = input().split()
            if curso == "EPR":
                alunos["EPR"] += 1
            elif curso == "EHD":
                alunos["EHD"] += 1
            else:
                alunos["INTRUSOS"] += 1

        for k in alunos:
            print(f"{k}: {alunos[k]}")
    
    except EOFError:
        break
