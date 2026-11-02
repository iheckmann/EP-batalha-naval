def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []

    if orientacao == "horizontal":
        for i in range(tamanho):
            posicoes.append([linha, coluna + i])

    elif orientacao == "vertical":
        for i in range(tamanho):
            posicoes.append([linha + i, coluna])

    return posicoes

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    novo_navio = define_posicoes(linha, coluna, orientacao, tamanho)

    if nome_navio in frota:
        frota[nome_navio].append(novo_navio)
    else:
        frota[nome_navio] = [novo_navio]
        
    return frota

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = "X"
        
    else:
        tabuleiro[linha][coluna] = "-"
    
    return tabuleiro

def posiciona_frota(frota):
    tabuleiro = [[0] * 10 for _ in range(10)]

    for navio in frota:
        for posicoes in frota[navio]:
            for posicao in posicoes:
                linha, coluna = posicao
                tabuleiro[linha][coluna] = 1

    return tabuleiro

def afundados(frota, tabuleiro):
    navios_afundados = 0

    for navio in frota:
        for posicoes in frota[navio]:
            afundado = True
            for posicao in posicoes:
                linha, coluna = posicao
                if tabuleiro[linha][coluna] != "X":
                    afundado = False
                    break
            if afundado:
                navios_afundados += 1

    return navios_afundados

def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)

    for posicao in posicoes:
        linha_pos, coluna_pos = posicao
        if linha_pos < 0 or linha_pos >= 10 or coluna_pos < 0 or coluna_pos >= 10:
            return False

        for navio in frota:
            for posicoes_navio in frota[navio]:
                if posicao in posicoes_navio:
                    return False

    return True
