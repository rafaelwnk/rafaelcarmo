dados = [("Ana", 8), ("João", 7), ("Ana", 10), ("Bia", 9)]

notas = {}

for nome, nota in dados:
    notas.setdefault(nome, []).append(nota)

medias = {nome: sum(notas[nome]) / len(notas[nome]) for nome in notas}

ordenado = sorted(medias.items(), key=lambda x: x[1])

print("alunos ordenados pela média (ordem crescente):\n")
for nome, media in ordenado:
    print(f"{nome}: {media:.2f}")