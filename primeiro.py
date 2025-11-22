def primo(num):
    if num <= 1:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
    
    return True

lista = []

print('digite os números pra adicionar a lista (10 números)\n')
for i in range(10):
    num = int(input(f'digite o número {i+1}: '))
    lista.append(num)

primos = [n for n in lista if primo(n)]
nao_primos = [n for n in lista if not primo(n)]

print('\nlista de primos:', primos)
print('\nlista de não primos:', nao_primos)
