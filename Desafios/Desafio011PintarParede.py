# Solicita ao usuário que insira a largura e a altura da parede em metros
largura = float(input("Digite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede em metros: "))

# Calcula a área da parede em metros quadrados
area = largura * altura

# Define a quantidade de metros quadrados que 1 litro de tinta pode pintar
metros_por_litro = 2

# Calcula a quantidade de tinta necessária em litros
quantidade_tinta = area / metros_por_litro

# Exibe a quantidade de tinta necessária para pintar a parede
print(f"Para pintar uma parede de {largura}m de largura por {
      altura}m de altura, você precisará de {quantidade_tinta:.2f} litros de tinta.")
