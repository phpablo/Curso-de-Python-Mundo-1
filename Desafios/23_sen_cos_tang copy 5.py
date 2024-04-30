import math

# Solicita ao usuário que insira o valor do ângulo em graus
angulo_graus = float(input("Digite o valor do ângulo em graus: "))

# Converte o ângulo de graus para radianos
angulo_radianos = math.radians(angulo_graus)

# Calcula o seno, cosseno e tangente do ângulo
seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)

# Mostra na tela os valores do seno, cosseno e tangente do ângulo
print(f"O seno do ângulo é: {seno:.2f}")
print(f"O cosseno do ângulo é: {cosseno:.2f}")
print(f"A tangente do ângulo é: {tangente:.2f}")
