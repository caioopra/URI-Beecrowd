N = int(input())

horas = N // 3600
minutos = (N % 3600) // 60
segundos = N % 3600 % 60   
print("{}:{}:{}".format(horas, minutos, segundos))