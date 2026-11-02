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


configuracao_navios = [
    ("porta-aviões", 4, 1),
    ("navio-tanque", 3, 2),
    ("contratorpedeiro", 2, 3),
    ("submarino", 1, 4)
]

frota = {}

for nome, tamanho, quantidade in configuracao_navios:
    navios_alocados = 0
    
    while navios_alocados < quantidade:
        print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
        
        linha = int(input("Linha: "))
        coluna = int(input("Coluna: "))
        
        if tamanho == 1:
            orientacao = "horizontal"
        else:
            opcao_orientacao = int(input(" [1] Vertical [2] Horizontal >"))
            if opcao_orientacao == 1:
                orientacao = "vertical"
            else:
                orientacao = "horizontal"
        
        if posicao_valida(frota, linha, coluna, orientacao, tamanho):
            frota = preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
            navios_alocados += 1
        else:
            print("Esta posição não está válida!")

print(frota)
