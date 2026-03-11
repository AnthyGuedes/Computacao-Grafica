
p1 = [6,8]
p2 = [4,5]
p3 = [8,5]

Tx = 3
Ty = -4

def translacao(pontos, Tx, Ty):

    pontos_translados = []

    for ponto in pontos:
        novo_x = ponto[0] + Tx
        novo_y = ponto[1] + Ty

        pontos_translados.append([novo_x, novo_y])

    return pontos_translados

pontos_original = [p1,p2,p3]

novos_pontos = translacao(pontos_original, Tx, Ty)

print("Novoas pontos ->", novos_pontos)


def escala(pontos, Sx, Sy):
    pontos_escalados = []

    for ponto in pontos:

        novo_x = ponto[0] * Sx


        novo_y = ponto[1] * Sy

        # Guarda o novo ponto na lista
        pontos_escalados.append([novo_x, novo_y])

    return pontos_escalados



p1 = [2, 2]
p2 = [4, 4]

Sx = 2
Sy = 2


novos_pontos = escala([p1, p2], Sx, Sy)

print("Pontos escalados ->", novos_pontos)