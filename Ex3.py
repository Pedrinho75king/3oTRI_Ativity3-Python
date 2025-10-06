valores = [
    10,
    3 + 2j,
    True,
    "Pedrinho",
    [1,5],
    2.61,
    None,
    (3,5),
    {1,5},
    {"chave": "valor", "idade": 25}
]

for valor in valores:
    print (f"Valor: {valor} - Tipo: {type(valor)}")