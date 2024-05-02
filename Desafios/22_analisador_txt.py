# nome = input('Digite seu nome completo:')
# nomeUpper = nome.upper()
# nomeLower = nome.lower()
# nomeNoSpace = nome.replace(' ','')
# nomeStart = nome.split()
# nomeStart2 = nomeStart[0]
# nomeCount = len(nomeNoSpace)
# nomeStartCount = len(nomeStart2)
# print('\nSeu nome é ' + nome + '\n')
# print('Seu nome em maiúsculo é ' + nomeUpper + '\n')
# print('Seu nome em minúsculo é ' + nomeLower + '\n')
# print('Seu nome possui ' + str(nomeCount) + ' letras\n')
# print('Seu primeiro nome é ' + nomeStart2 + '\n')
# print('Seu nome possui ' + str(strnomeStartCount) + ' letras\n')

# REFATORANDO

nome = str(input('Digite seu nome completo: ')).strip()
print('===Analisando seu nome===')
print(f'Seu nome em maiúsculo é {nome.upper()}')
print(f'Seu nome em minúsculo é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome) - nome.count(' ')}')
print(f'Seu primeiro nome tem {nome.find(' ')}')