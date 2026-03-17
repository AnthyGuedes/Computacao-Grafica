Po = [-2, 4, 1, 1]  # pontos (x, y, z, w)
Tx = 5
Ty = 2
Tz = 3

matriz = [
    [1, 0, 0, Tx],
    [0, 1, 0, Ty],
    [0, 0, 1, Tz],
    [0, 0, 0, 1 ]
]


Pu = [0, 0, 0, 0]


for i in range(4): # linha
    soma = 0
    for j in range(4): # coluna
        soma += matriz[i][j] * Po[j]
    Pu[i] = soma


print("--- Matriz de Translação 4x4 (Mt) ---")
for linha in matriz:
    print(linha)

print("\nPonto Original (Po) ->", Po)
print("Ponto Translado (Pu) ->", Pu)