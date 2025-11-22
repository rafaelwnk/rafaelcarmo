produtos = {
    "Alimentação": [12.50, 8.99, 15.30],
    "Limpeza": [5.20, 7.80],
    "Higiene": [10.00, 12.00, 9.50, 14.00]
}

medias = {}

for categoria, precos in produtos.items():
    medias[categoria] = sum(precos) / len(precos)

categoria, media = max(medias.items(), key=lambda x: x[1])
print(f'a categoria mais cara em média é: {categoria} ({media:.2f})')