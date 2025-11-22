num = input('digite um número: ')

try:
    num_convertido = float(num)
    
    if not num_convertido.is_integer():
        print(f'inteiro: {num_convertido:.0f}, decimal: {num_convertido}')
    else:
        print("o número é par" if num_convertido % 2 == 0 else "o número é impar")

except ValueError:
    print('não é possível converter a entrada digitada para float')