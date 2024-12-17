def adicao(x,y)
return x+y

def subtracao (x,y)
return x-y

def multiplicacao (x,y)
return x*y

def divisao (x,y)
return x/y

def calculadora():
    print("selecione a operação: ")
    print(1.adicao)
    print(2.subtracao)
    print(3.multiplicacao)
    prit(4.divisao)

while true:
    escolha = input("Escolha 1/2/3/4): "))
    if Escolha in ('1','2','3','4'):
    x= int(input("Digite o primeiro número: "))
    y= int(input("digite o segundo número: "))
    if escolha =='1':
     print("resultaado: ", adicao(x,y))
    if escolha =='2'
    print("resultado: ", subtracao(x-y))
    if escolha =='3'
    print("resultado: ", multiplicacao(x*y))
    if escolha =='4'
    if y !=0
    print("resultado: ",divisao(x/y))
    else:
        print("não é permitidaa divisão por zero")
else:
    print("Escolha inválida")

continuar= printar("deseja fazer outra operação? (s/n)")
if cintinuar == "n":]print("Calculadora Encerrada")
break;

Calculadora()

