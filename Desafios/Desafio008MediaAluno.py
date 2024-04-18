# Solicita ao usuário que insira o valor em metros
metros = float(input("Digite o valor em metros: "))

# Converte metros para centímetros e milímetros
centimetros = metros * 100
milimetros = metros * 1000

# Exibe os resultados na tela
print(f"{metros} metros equivalem a {centimetros} centímetros.")
print(f"{metros} metros equivalem a {milimetros} milímetros.")
