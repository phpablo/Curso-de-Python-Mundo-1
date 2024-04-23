# Solicita ao usuário que insira o preço do produto
preco_produto = float(input("Digite o preço do produto: "))

# Calcula o novo preço com desconto de 5%
novo_preco = preco_produto * 0.95  # 95% do preço original

# Exibe o novo preço com desconto
print(f"O novo preço do produto com 5% de desconto é R${novo_preco:.2f}")
