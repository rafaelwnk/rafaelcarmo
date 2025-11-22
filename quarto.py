def produto_escalar(vetor1, vetor2):
    return sum(x * y for x, y in zip(vetor1, vetor2))

vetor1 = []
vetor2 = []

tamanho = int(input('digite o tamanho que deseja pros vetores: '))

print('digite os valores do primeiro vetor: ')
for i in range(tamanho):
    vetor1.append(int(input(f'digite o valor {i+1}: ')))

print('\ndigite os valores do segundo vetor: ')
for i in range(tamanho):
    vetor2.append(int(input(f'digite o valor {i+1}: ')))

resultado = produto_escalar(vetor1, vetor2)
print(f'\no produto escalar entre os dois vetores é igual a: {resultado}')