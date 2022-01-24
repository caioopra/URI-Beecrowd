# https://www.beecrowd.com.br/judge/pt/problems/view/2409
def passa_na_porta(a, b, c, h, l):
    if a <= h and b <= l:
        return 'S'
    elif a <= h and c <= l:
        return 'S'
    elif b <= h and a <= l:
        return 'S'
    elif b <= h and c <= l:
        return 'S'
    elif c <= h and a <= l:
        return 'S'
    elif c <= h and b <= l:
        return 'S'
    else:
        return 'N'

a, b, c = [int(x) for x in input().split()]
h, l = [int(x) for x in input().split()]

print(passa_na_porta(a, b, c, h, l))
