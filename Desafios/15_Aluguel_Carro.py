# Solicita ao usuário que insira a quantidade de quilômetros percorridos e a quantidade de dias de aluguel do carro
km_percorridos = float(
    input("Digite a quantidade de quilômetros percorridos: "))
dias_aluguel = int(input("Digite a quantidade de dias de aluguel do carro: "))

# Define o preço por dia de aluguel e por quilômetro rodado
preco_por_dia = 60
preco_por_km = 0.15

# Calcula o preço total a pagar
preco_total = (preco_por_dia * dias_aluguel) + (preco_por_km * km_percorridos)

# Exibe o preço total a pagar
print(f"O preço total a pagar pelo aluguel do carro é R${preco_total:.2f}")

m