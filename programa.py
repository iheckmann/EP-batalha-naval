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

def posiciona_frota(frota):
    tabuleiro = [[0] * 10 for _ in range(10)]
    for navio in frota:
        for posicoes in frota[navio]:
            for posicao in posicoes:
                linha, coluna = posicao
                tabuleiro[linha][coluna] = 1
    return tabuleiro


def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = "X"
    else:
        tabuleiro[linha][coluna] = "-"
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


def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto



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
            opcao_orientacao = int(input("Orientação: [1] Vertical [2] Horizontal >"))
            if opcao_orientacao == 1:
                orientacao = "vertical"
            else:
                orientacao = "horizontal"
        
        if posicao_valida(frota, linha, coluna, orientacao, tamanho):
            frota = preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
            navios_alocados += 1
        else:
            print("Esta posição não está válida!")

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_jogador = posiciona_frota(frota)
tabuleiro_oponente = posiciona_frota(frota_oponente)

jogadas_feitas = []
jogando = True


while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    while True:
        linha = int(input("Jogador, qual linha deseja atacar? "))
        while linha < 0 or linha > 9:
            print("Linha inválida!")
            linha = int(input("Jogador, qual linha deseja atacar? "))

        coluna = int(input("Jogador, qual coluna deseja atacar? "))
        while coluna < 0 or coluna > 9:
            print("Coluna inválida!")
            coluna = int(input("Jogador, qual coluna deseja atacar? "))

        if [linha, coluna] in jogadas_feitas:
            print(f"A posição linha {linha} e coluna {coluna} já foi informada anteriormente!")
        else:
            break

    jogadas_feitas.append([linha, coluna])
    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)

    if afundados(frota_oponente, tabuleiro_oponente) == 10:
        print("Parabéns! Você derrubou todos os navios do seu oponente!")
        jogando = False