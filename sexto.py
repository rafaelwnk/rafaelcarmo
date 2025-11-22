from collections import Counter

frase = input('digite uma frase: ')
frase = frase.replace(" ", "")

frequencias = Counter(frase).most_common()

if len(frequencias) >= 3:
    frequencia_terceiro = frequencias[2][1]

    terceiro_caracteres = [char for char, freq in frequencias if freq == frequencia_terceiro]

    if len(terceiro_caracteres) == 1:
        print(f"o 3° caractere mais frequente é: '{terceiro_caracteres[0]}' e aparece {frequencia_terceiro} vezes")
    else:
        chars = "', '".join(terceiro_caracteres)
        print(f"houve empate no 3° lugar, os caracteres são: '{chars}', cada um aparece {frequencia_terceiro} vezes")
    
else:
    print("há menos de 3 caracteres únicos na frase")