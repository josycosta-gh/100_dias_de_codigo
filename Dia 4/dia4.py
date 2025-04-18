def adicao(x,y):
    return x+y

def subtracao(x,y):
    return x-y

def multiplicacao(x,y):
    return x*y

def divisao(x,y):
    return x/y


def calculadora():
    print("Selecione a operação!")
    print("1.Adicao")
    print("2.Subtracao")
    print("3.Multiplicacao")
    print("4.Divisao")

    while True: 
        escolha = input("escolha(1/2/3/4)")
        if escolha in ('1', '2', '3', '4'):
          x = int(input("Digite o primeiro número"))
          y = int(input("digite o segundo número"))
          if escolha == '1':
            print("Resultado ", adicao(x,y))

          if escolha == '2':
            print("Resultado ", subtracao(x,y))

          if escolha == '3':
            print("Resultado ", multiplicacao(x,y))

          if escolha == '4':
            if y !=0:
              print("Resultado ", divisao(x,y))
          else:
             print("A divisão não é permitida por zero")
        else:
           print("escolha inválida")

        continuar = input("deseja fazer outra operação? (s/n)")
        if continuar == "n":
          print("calculadora encerrada")
          break;

calculadora;
