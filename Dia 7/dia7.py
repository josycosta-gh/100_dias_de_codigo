def gerar_tabuada(numero):
    print (f"tabuada do {numero}")
    for i in range (1,11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
    
#Soliciar ao usuário que insira um numero
numero = int(input("Digite um número para gerar a tabuada: "))

#chamar a funcao para gerar a tabuada
gerar_tabuada(numero)

