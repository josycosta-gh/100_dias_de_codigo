from sympy import numer


def fatorial(n):
    if n==0 or n==1:
        return 1
    else:
        resultado=1
        for i in range(2, n +1):
            resultado= resultado * 1
            return resultado

num = int(input("Digite um número: "))
if num < 0:
    print (f"o fatorial de {num} não existe")

else:
    print (f"ofatorial de {num} é {fatorial(num)}")
