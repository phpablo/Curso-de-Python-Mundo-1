# Solicita ao usuário que insira a temperatura em graus Celsius
celsius = float(input("Digite a temperatura em graus Celsius: "))

# Converte a temperatura de Celsius para Fahrenheit 
fahrenheit = (celsius * 9/5) + 32

# Exibe a temperatura convertida em Fahrenheit
print('A temperatura de {} graus Celsius equivale a {} graus Fahrenheit.'.format(celsius, fahrenheit))
