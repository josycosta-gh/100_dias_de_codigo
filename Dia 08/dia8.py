def c_p_f(celsius):
    fahreinheit = (celsius * 9/5) + 32
    return fahreinheit

entrada = float(input("Digite a temperatura em Grau Celsius:"))

print(f"A temperatura em fahrenheit é: {c_p_f(entrada)}")
