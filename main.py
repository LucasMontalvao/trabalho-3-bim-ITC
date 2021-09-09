from random import randrange

cidades = [0,  # Aracaju
           1,  # Belém
           2,  # B. Horizonte
           3,  # Boa Vista
           4,  # Brasília
           5,  # C. Grande
           6,  # Cuiabá
           7,  # Curitiba
           8,  # Florianópolis
           9,  # Fortaleza
           10,  # Goiânia
           11,  # João Pessoa
           12,  # Macapá
           13,  # Maceió
           14,  # Manaus
           15,  # Natal
           16,  # Palmas
           17,  # Porto Alegre
           18,  # Porto Velho
           19,  # Recife
           20,  # Rio Branco
           21,  # R. Janeiro
           22,  # Salvador
           23,  # São Luis
           24,  # São Paulo
           25,  # Teresina
           26]  # Vitória

matriz_distancias = [[0,    2079, 1578, 6000, 1652,  # Distancias Aracaju
                      2765, 2775, 2595, 2892, 1183,
                      1848, 611,  9999, 294,  521,
                      788,  1662, 3296, 4230, 501,
                      4763, 1855, 356,  1578, 2187,
                      1142, 1408],

                     [2079, 0,    2824, 6083, 2120,  # Distancias Belém
                      2942, 2941, 3193, 3500, 1610,
                      2017, 2161, 9999, 2173, 5298,
                      2108, 1283, 3852, 4397, 2074,
                      4931, 3250, 2100, 806,  2933,
                      947, 3108],

                     [1578, 2824, 0,    4736, 716,  # Distancias BHorizonte
                      1453, 1594, 1004, 1301, 2528,
                      906,  2171, 9999, 1854, 3951,
                      2348, 1690, 1712, 3050, 2061,
                      3584, 434,  1372, 2738, 586,
                      2302, 524],

                     [6000, 6083, 4736, 0,    4275,  # Distancias Boa Vista
                      3836, 3142, 4821, 5128, 6548,
                      4076, 6593, 9999, 6279, 785,
                      6770, 4926, 5348, 1686, 6483,
                      2230, 5159, 5794, 6120, 4756,
                      6052, 5261],

                     [1652, 2120, 716,  4275, 0,  # Distancias Brasilia
                      1134, 1133, 1366, 1673, 2200,
                      209,  2245, 9999, 1930, 3490,
                      2422, 973,  2027, 2589, 2135,
                      3123, 1148, 1446, 2157, 1015,
                      1789, 1239],

                     [2765, 2942, 1453, 3836, 1134,  # Distancias C Grande
                      0,    694,   991, 1298, 3407,
                      935,  3357, 9999, 3040, 3051,
                      3534, 1785, 1518, 2150, 3247,
                      2684, 1444, 2568, 2979, 1014,
                      2911, 1892],

                     [2595, 3193, 1004, 4821, 1366,  # Distancias Curitiba
                      991,  1679, 0,    300,  3541,
                      1186, 3188, 9999, 2871, 4036,
                      3365, 2036, 711,  3135, 3078,
                      3669, 852,  2385, 3230, 408,
                      3143, 1300],

                     [2775, 2941, 1594, 3142, 1133,  # Distancias Cuiaba
                      694,   0,   1679, 1986, 3406,
                      934,  3366, 9999, 3049, 2357,
                      3543, 1784, 2206, 145,  3255,
                      1990, 2017, 2566, 2978, 1614,
                      2910, 2119],

                     [2595, 3193, 1004,  4821, 1366,  # Distancias Florianopolis
                      991,  1679, 0,     300,  3541,
                      1186, 3188, 9999,  2871, 4036,
                      3365, 2036, 711,   3135, 3078,
                      3669, 852,   2385, 3230, 408,
                      3143, 1300],

                     [1183, 1610, 2528, 6548, 2200,  # Distancias Fortaleza
                      3407, 3406, 3541, 3838, 0,
                      2482, 688,  9999, 1075, 5763,
                      537,  2035, 4242, 4862, 800,
                      5396, 2805, 1389, 1070, 3127,
                      634,  2397],

                     [1848, 2017, 906,  4076, 209,  # Distancias Goiânia
                      935,  934,  1186, 1493, 2482,
                      0,    2442, 9999, 2125, 3291,
                      2618, 874,  1847, 2390, 2332,
                      2924, 1338, 1643, 2054, 926,
                      1986, 1428],

                     [611,  2161, 2171, 6593, 2245,  # Distancais João Pessoa
                      3357, 3366, 3188, 3485, 688,
                      2442, 0,    9999, 395,  5808,
                      185,  2253, 3889, 4822, 120,
                      5356, 2448, 949,  1660, 2770,
                      1224, 2001],

                     [9999, 9999, 9999, 9999, 9999,  # Distancias Macapa que a principio é uma cidade flutuante
                      9999, 9999, 9999, 9999, 9999,
                      9999, 9999, 0,    9999, 9999,
                      9999, 9999, 9999, 9999, 9999,
                      9999, 9999, 9999, 9999, 9999,
                      9999, 9999],

                     [294,  2173, 1854, 6279, 1930,  # Distancias Maceió
                      3040, 3049, 2871, 3168, 1075,
                      2125, 395,  9999, 0,    5491,
                      572,  1851, 3572, 4505, 285,
                      5039, 2131, 632,  1672, 2453,
                      1236, 1684],

                     [5215, 5298, 3951, 785,  3490,  # Distancias Manaus
                      3051, 2357, 4036, 4443, 5763,
                      3291, 5808, 9999, 5491, 0,
                      5985, 4141, 4563, 901,  5698,
                      1445, 4374, 5009, 5335, 3971,
                      5267, 4476],

                     [788,  2108, 2348, 6770, 2422,  # Distancia Natal
                      3534, 3543, 3365, 3662, 537,
                      2618, 185,  9999, 572,  5985,
                      0,    2345, 4066, 4998, 297,
                      5533, 2625, 1126, 1607, 2947,
                      1171, 2178],

                     [1662, 1283, 1690, 4926, 973,  # Distancia Palmas
                      1785, 1784, 2036, 2336, 2035,
                      874,  2253, 9999, 1851, 4141,
                      2345, 0,    2747, 9999, 2058,
                      3764, 2124, 1454, 1386, 1776,
                      1401, 2214],

                     [3296, 3852, 1712, 5348, 2027,  # Distancia Porto Alegre
                      1518, 2206, 711,  476,  4242,
                      1847, 3889, 9999, 3572, 4563,
                      4066, 2747, 0,    3662, 3779,
                      4196, 1553, 3090, 3891, 1109,
                      3804, 2001],

                     [4230, 4397, 3050, 1686, 2589,  # Distancia Porto Velho
                      2150, 1456, 3135, 3442, 4862,
                      2390, 4822, 9999, 4505, 901,
                      4998, 0,    3662, 0,    4712,
                      544,  3473, 4023, 4434, 3070,
                      4366, 3575],

                     [501,  2074, 2061, 6483, 2135,  # Distancia Recife
                      3247, 3255, 3078, 3375, 800,
                      2332, 120,  9999, 285,  5698,
                      297,  2058, 3779, 4712, 0,
                      5243, 2338, 839,  1573, 2660,
                      1137, 1831],

                     [4763, 4931, 3584, 2230, 3123,  # Distancia Rio Branco
                      2684, 1990, 3669, 3976, 5396,
                      2924, 5356, 9999, 5039, 1445,
                      5533, 3764, 4196, 544,  5243,
                      0,    4007, 4457, 4968, 3604,
                      4900, 4109],

                     [1855, 3250, 434,  5159, 1148,  # Distancia Rio de Janeiro
                      1444, 2017, 852,  1144, 2805,
                      1338, 2448, 9999, 2131, 4374,
                      2625, 2124, 1553, 3473, 2338,
                      4007, 0,    1649, 3015, 429,
                      2579, 521],

                     [356,  2100, 1372, 5794, 1446,  # Distancia Salvador
                      2568, 2566, 2385, 2682, 1389,
                      1643, 949,  9999, 632,  5009,
                      1126, 1454, 3090, 4023, 839,
                      4457, 1649, 0,    1599, 1962,
                      1163, 1202],

                     [1578, 806,  2738, 6120, 2157,  # Distancia São Luis
                      2979, 2978, 3230, 3537, 1070,
                      2054, 1660, 9999, 1672, 5335,
                      1607, 1386, 3891, 4434, 1573,
                      4968, 3015, 1599, 0,    2970,
                      446,  2607],

                     [2187, 2933, 586,  4756, 1015,  # Distancia São Paulo
                      1014, 1614, 408,   705, 3127,
                      926,  2770, 9999, 2453, 3971,
                      2947, 1776, 1109, 3070, 2660,
                      3604, 429,  1962, 2970, 0,
                      2792, 882],

                     [1142, 947,  2302, 6052, 1789,  # Distancia Teresina
                      2911, 2910, 3143, 3450, 634,
                      1986, 1224, 9999, 1236, 5267,
                      1171, 1401, 3804, 4366, 1137,
                      4900, 2579, 1163, 446,  2792,
                      0,    2171],

                     [1408, 3108, 524,  5261, 1239,  # Distancia Vitória
                      1892, 2119, 1300, 1597, 2397,
                      1428, 2001, 9999, 1684, 4476,
                      2178, 2214, 2001, 3575, 1831,
                      4109, 521,  1202, 2607, 882,
                      2171, 0]]

def funcao_objetivo(solucao):
    distancia = 0
    for i in range(0, len(solucao) - 1):
        x = solucao[i]
        y = solucao[i + 1]
        distancia_cidade = matriz_distancias[x][y]
        distancia = distancia + distancia_cidade
    return distancia + matriz_distancias[solucao[len(solucao) - 1]][solucao[0]]


def algoritmo_aleatorio():
    solucao = []
    cidades_copia = []

    for i in cidades:
        cidades_copia.append(i)

    while len(cidades_copia) > 0:
        indice = randrange(len(cidades_copia))
        cidade_sorteada = cidades_copia[indice]
        del cidades_copia[indice]
        solucao.append(cidade_sorteada)

    print("Solução final :", solucao, " Distancia = ", funcao_objetivo(solucao))


def algoritmo_guloso():
    solucao = []
    cidades_copia = []

    for i in cidades:
        cidades_copia.append(i)

    # Seleciona a cidade de partida
    indice = randrange(len(cidades_copia))
    cidade_sorteada = cidades_copia[indice]
    del cidades_copia[indice]
    solucao.append(cidade_sorteada)

    while len(cidades_copia) > 0:
        cidade_de_onde_esta_saindo = cidades[solucao[len(solucao) - 1]]
        cidade_mais_proxima = cidades_copia[0]
        cidade_mais_proxima_indice = 0
        menor_distancia = matriz_distancias[cidade_de_onde_esta_saindo][cidade_mais_proxima]
        # print("------")
        # print("Cidade de onde esta saindo:",cidade_de_onde_esta_saindo)
        i = 0
        for proxima_cidade_candidata in cidades_copia:
            distancia = matriz_distancias[cidade_de_onde_esta_saindo][proxima_cidade_candidata]
            # print("Cidade",cidades[proxima_cidade_candidata]," distancia ",distancia)
            if distancia < menor_distancia:
                menor_distancia = distancia
                cidade_mais_proxima = proxima_cidade_candidata
                cidade_mais_proxima_indice = i
            i = i + 1
        # print("Cidade mais proxima:",cidade_mais_proxima,"Distancia",menor_distancia)

        solucao.append(cidades_copia[cidade_mais_proxima_indice])
        del cidades_copia[cidade_mais_proxima_indice]

    print("Solução final :", solucao, " Distancia = ", funcao_objetivo(solucao))


def algoritmo_semi_guloso():
    solucao = []
    cidades_copia = []
    delta = 70

    for i in cidades:
        cidades_copia.append(i)

    # Seleciona a cidade de partida
    indice = randrange(len(cidades_copia))
    cidade_sorteada = cidades_copia[indice]
    del cidades_copia[indice]
    solucao.append(cidade_sorteada)

    while len(cidades_copia) > 0:
        # Sortea a probabilidade de selecionar o método guloso ou aleatorio.
        valor_aleatorio = randrange(100)

        if delta > valor_aleatorio:
            # -------
            # . Metodo Guloso
            # -------
            #print("Metodo Guloso")
            cidade_de_onde_esta_saindo = cidades[solucao[len(solucao) - 1]]
            cidade_mais_proxima = cidades_copia[0]
            cidade_mais_proxima_indice = 0
            menor_distancia = matriz_distancias[cidade_de_onde_esta_saindo][cidade_mais_proxima]
            # print("------")
            # print("Cidade de onde esta saindo:",cidade_de_onde_esta_saindo)
            i = 0
            for proxima_cidade_candidata in cidades_copia:
                distancia = matriz_distancias[cidade_de_onde_esta_saindo][proxima_cidade_candidata]
                # print("Cidade",cidades[proxima_cidade_candidata]," distancia ",distancia)
                if distancia < menor_distancia:
                    menor_distancia = distancia
                    cidade_mais_proxima = proxima_cidade_candidata
                    cidade_mais_proxima_indice = i
                i = i + 1
            # print("Cidade mais proxima:",cidade_mais_proxima,"Distancia",menor_distancia)

            solucao.append(cidades_copia[cidade_mais_proxima_indice])
            del cidades_copia[cidade_mais_proxima_indice]
        else:
            # -------
            # . Metodo Aleatório
            # -------
            # print("Metodo Aleatório")
            indice = randrange(len(cidades_copia))
            cidade_sorteada = cidades_copia[indice]
            del cidades_copia[indice]
            solucao.append(cidade_sorteada)

    print("Solução final :", solucao, " Distancia = ", funcao_objetivo(solucao))


# execucao = 30
# while execucao > 0:
#    algoritmo_aleatorio()
#    execucao -= 1

# execucao = 30
# while execucao > 0:
#    algoritmo_guloso()
#    execucao -= 1

execucao = 30
while execucao > 0:
    algoritmo_semi_guloso()
    execucao -= 1