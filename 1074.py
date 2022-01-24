quantidade = int(input())

for i in range(quantidade):
    entrada = int(input())

    if entrada % 2 == 0:
        if entrada > 0:
            print("EVEN POSITIVE")
        elif entrada < 0:
            print("EVEN NEGATIVE")
        else:
            print("NULL")
    else:
        if entrada > 0:
            print("ODD POSITIVE")
        else:
            print("ODD NEGATIVE")
