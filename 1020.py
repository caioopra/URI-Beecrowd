idadeDias = int(input())

anos = idadeDias // 365
meses = (idadeDias % 365) // 30
dias = (idadeDias % 365) % 30

print("{} ano(s)".format(anos))
print("{} mes(es)".format(meses))
print("{} dia(s)".format(dias))
