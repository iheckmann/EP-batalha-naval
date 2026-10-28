def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []

    if orientacao == "horizontal":
        for i in range(tamanho):
            posicoes.append([linha, coluna + i])

    elif orientacao == "vertical":
        for i in range(tamanho):
            posicoes.append([linha + i, coluna])

    return posicoes