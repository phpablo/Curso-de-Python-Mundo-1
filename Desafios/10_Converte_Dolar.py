# Solicita ao usuário que insira o valor em reais na carteira
valor_em_reais = float(
    input("Digite o valor em reais que você tem na carteira: "))

# Define a cotação atual do dólar
cotacao_dolar = 5.0  # Por exemplo, considerando 1 dólar = 5 reais

# Calcula quantos dólares a pessoa pode comprar
quantidade_dolares = valor_em_reais / cotacao_dolar

# Exibe a quantidade de dólares que a pessoa pode comprar
print(f"Com R${valor_em_reais:.2f} você pode comprar US${
      quantidade_dolares:.2f}")
