# Solicita ao usuário que insira o salário do funcionário
salario_atual = float(input("Digite o salário do funcionário: "))

# Calcula o novo salário com aumento de 15%
novo_salario = salario_atual * 1.15  # 115% do salário original

# Exibe o novo salário com o aumento
print(f"O novo salário do funcionário com 15% de aumento é R${novo_salario:.2f}")