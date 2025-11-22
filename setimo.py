livros = [
    {"titulo": "A", "ano": 2020, "preco": 45},
    {"titulo": "B", "ano": 2024, "preco": 80},
    {"titulo": "C", "ano": 2020, "preco": 50},
    {"titulo": "D", "ano": 2022, "preco": 40}
]

livros_por_ano = {}

for livro in livros:
    ano = livro["ano"]
    if ano not in livros_por_ano:
        livros_por_ano[ano] = []
    livros_por_ano[ano].append(livro)

for ano in sorted(livros_por_ano):
    livros_do_ano = livros_por_ano[ano]
    preco_medio = sum(l["preco"] for l in livros_do_ano) / len(livros_do_ano)
    titulos = ", ".join(l["titulo"] for l in livros_do_ano)
    print(f"Ano {ano}: livros = {titulos}; preço médio = R$ {preco_medio:.2f}")