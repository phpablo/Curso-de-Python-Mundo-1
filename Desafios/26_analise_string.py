frase = str(input('Digite uma frase ')).upper().strip()
print(f'Letra A aparece {frase.count('A')} vezes')
print(f'A primeira letra A apareceu na posição {frase.find('A')+1}')
print(f'A ultima letra A apareceu na posição {frase.rfind('A')+1}')