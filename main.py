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

matriz_distancias = [[0,      2.079, 1.578, 6.000, 1.652,  # Distancias Aracaju
                      2.765,  2.775, 2.595, 2.892, 1.183,
                      1.848,  611,   0,     294,   5.21,
                      788,    1.662, 3.296, 4.230, 501,
                      4.763,  1.855, 356,   1.578, 2.187,
                      1.142,  1.408],

                     [2.079, 0,     2.824, 6.083, 2.120,  # Distancias Belém
                      2.942, 2.941, 3.193, 3.500, 1.610,
                      2.017, 2.161, 0,     2.173, 5.298,
                      2.108, 1.283, 3.852, 4.397, 2.074,
                      4.931, 3.250, 2.100, 806,   2.933,
                      947,   3.108],

                     [1.578, 2.824, 0,     4.736, 716,   # Distancias B.Horizonte
                      1.453, 1.594, 1.004, 1.301, 2.528,
                      906,   2.171, 0,     1.854, 3.951,
                      2.348, 1.690, 1.712, 3.050, 2.061,
                      3.584, 434,   1.372, 2.738, 586,
                      2.302, 524],

                     [6.000, 6.083, 4.736, 0,     4.275,  # Distancias Boa Vista
                      3.836, 3.142, 4.821, 5.128, 6.548,
                      4.076, 6.593, 0,     6.279, 785,
                      6.770, 4.926, 5.348, 1.686, 6.483,
                      2.230, 5.159, 5.794, 6.120, 4.756,
                      6.052, 5.261],

                     [1.652, 2.120,	716,   4.275, 0,     # Distancias Brasilia
                      1.134, 1.133, 1.366, 1.673, 2.200,
                      209,   2.245, 0,     1.930, 3.490,
                      2.422, 973,   2.027, 2.589, 2.135,
                      3.123, 1.148, 1.446, 2.157, 1.015,
                      1.789, 1.239],

                     [2.765, 2.942, 1.453, 3.836, 1.134,  # Distancias C Grande
                      0,     694,   991,   1.298, 3.407,
                      935,   3.357, 0,     3.040, 3.051,
                      3.534, 1.785, 1.518, 2.150, 3.247,
                      2.684, 1.444, 2.568, 2.979, 1.014,
                      2.911, 1.892],

                     [2.775, 2.941, 1.594, 3.142, 1.133,  # Distancias Cuiaba
                      694,   0,     1.679, 1.986, 3.406,
                      934,   3.366, 0,     3.049, 2.357,
                      3.543, 1.784, 2.206, 1.45,  3.255,
                      1.990, 2.017, 2.566, 2.978, 1.614,
                      2.910, 2.119],

                     [2.595, 3.193, 1.004, 4.821, 1.366,  # Distancias Florianopolis
                      991,	 1.679,	0,     300,   3.541,
                      1.186, 3.188, 0,     2.871, 4.036,
                      3.365, 2.036, 711,   3.135, 3.078,
                      3.669, 852,   2.385, 3.230, 408,
                      3.143, 1.300],

                     [1.183, 1.610,	2.528, 6.548, 2.200,  # Distancias Fortaleza
                      3.407, 3.406,	3.541, 3.838, 0,
                      2.482, 688,   0,     1.075, 5.763,
                      537,   2.035, 4.242, 4.862, 800,
                      5.396, 2.805, 1.389, 1.070, 3.127,
                      634, 2.397],

                     [1.848, 2.017, 906,   4.076, 209,    # Distancias Goiânia
                      935,   934,	1.186, 1.493, 2.482,
                      0,     2.442, 0,     2.125, 3.291,
                      2.618, 874,   1.847, 2.390, 2.332,
                      2.924, 1.338, 1.643, 2.054, 926,
                      1.986, 1.428],

                     [611,   2.161, 2.171, 6.593, 2.245,  # Distancais João Pessoa
                      3.357, 3.366,	3.188, 3.485, 688,
                      2.442, 0,     0,     395,   5.808,
                      185,   2.253, 3.889, 4.822, 120,
                      5.356, 2.448, 949,   1.660, 2.770,
                      1.224, 2.001],

                     [0,     0,	    0,	   0,	  0,     # Distancias Macapa que a principio é uma cidade flutuante
                      0,	 0,	    0,	   0,	  0,
                      0,	 0,	    0,     0,     0,
                      0,     0,     0,     0,     0,
                      0,     0,     0,     0,     0,
                      0,     0],

                     [294,   2.173, 1.854, 6.279, 1.930,  # Distancias Maceió
                      3.040, 3.049, 2.871, 3.168, 1.075,
                      2.125, 395,   0,     0,     5.491,
                      572,   1.851, 3.572, 4.505, 285,
                      5.039, 2.131, 632,   1.672, 2.453,
                      1.236, 1.684],

                     [5.215, 5.298, 3.951, 785,   3.490,  # Distancias Manaus
                      3.051, 2.357, 4.036, 4.443, 5.763,
                      3.291, 5.808, 0,     5.491, 0,
                      5.985, 4.141, 4.563, 901,   5.698,
                      1.445, 4.374, 5.009, 5.335, 3.971,
                      5.267, 4.476],

                     [788,   2.108, 2.348, 6.770, 2.422,  # Distancia Natal
                      3.534, 3.543, 3.365, 3.662, 537,
                      2.618, 185,   0,     572,   5.985,
                      0,     2.345, 4.066, 4.998, 297,
                      5.533, 2.625, 1.126, 1.607, 2.947,
                      1.171, 2.178],

                     [1.662, 1.283, 1.690, 4.926, 973,  # Distancia Palmas
                      1.785, 1.784, 2.036, 2.336, 2.035,
                      874,   2.253, 0,     1.851, 4.141,
                      2.345, 0,     2.747, 0,     2.058,
                      3.764, 2.124, 1.454, 1.386, 1.776,
                      1.401, 2.214],

                     [3.296, 3.852, 1.712, 5.348, 2.027,  # Distancia Porto Alegre
                      1.518, 2.206, 711,   476,   4.242,
                      1.847, 3.889, 0,     3.572, 4.563,
                      4.066, 2.747, 0,     3.662, 3.779,
                      4.196, 1.553, 3.090, 3.891, 1.109,
                      3.804, 2.001],

                     [4.230, 4.397, 3.050, 1.686, 2.589,  # Distancia Porto Velho
                      2.150, 1.456, 3.135, 3.442, 4.862,
                      2.390, 4.822, 0,     4.505, 901,
                      4.998, 0,     3.662, 0,     4.712,
                      544,   3.473, 4.023, 4.434, 3.070,
                      4.366, 3.575],

                     [501,   2.074, 2.061, 6.483, 2.135,  # Distancia Recife
                      3.247, 3.255, 3.078, 3.375, 800,
                      2.332, 120,   0,     285,   5.698,
                      297,   2.058, 3.779, 4.712, 0,
                      5.243, 2.338, 839,   1.573, 2.660,
                      1.137, 1.831],

                     [4.763, 4.931, 3.584, 2.230, 3.123,  # Distancia Rio Branco
                      2.684, 1.990, 3.669, 3.976, 5.396,
                      2.924, 5.356, 0,     5.039, 1.445,
                      5.533, 3.764, 4.196, 544,   5.243,
                      0,     4.007, 4.457, 4.968, 3.604,
                      4.900, 4.109 ],

                     [1.855, 3.250, 434,   5.159, 1.148,  # Distancia Rio de Janeiro
                      1.444, 2.017, 852,   1.144, 2.805,
                      1.338, 2.448, 0,     2.131, 4.374,
                      2.625, 2.124, 1.553, 3.473, 2.338,
                      4.007, 0,     1.649, 3.015, 429,
                      2.579, 521],

                     [356,   2.100, 1.372, 5.794, 1.446,  # Distancia Salvador
                      2.568, 2.566, 2.385, 2.682, 1.389,
                      1.643, 949,   0,     632,   5.009,
                      1.126, 1.454, 3.090, 4.023, 839,
                      4.457, 1.649, 0,     1.599, 1.962,
                      1.163, 1.202],

                     [1.578, 806,   2.738, 6.120, 2.157,  # Distancia São Luis
                      2.979, 2.978, 3.230, 3.537, 1.070,
                      2.054, 1.660, 0,     1.672, 5.335,
                      1.607, 1.386, 3.891, 4.434, 1.573,
                      4.968, 3.015, 1.599, 0,     2.970,
                      446,   2.607],

                     [2.187, 2.933, 586,   4.756, 1.015,  # Distancia São Paulo
                      1.014, 1.614, 408,   705,   3.127,
                      926,   2.770, 0,     2.453, 3.971,
                      2.947, 1.776, 1.109, 3.070, 2.660,
                      3.604, 429,   1.962, 2.970, 0,
                      2.792, 882],

                     [1.142, 947,   2.302, 6.052, 1.789,  # Distancia Teresina
                      2.911, 2.910, 3.143, 3.450, 634,
                      1.986, 1.224, 0,     1.236, 5.267,
                      1.171, 1.401, 3.804, 4.366, 1.137,
                      4.900, 2.579, 1.163, 446,   2.792,
                      0, 2.171],

                     [1.408, 3.108, 524,   5.261, 1.239, # Distancia Vitória
                      1.892, 2.119, 1.300, 1.597, 2.397,
                      1.428, 2.001, 0,     1.684, 4.476,
                      2.178, 2.214, 2.001, 3.575, 1.831,
                      4.109, 521,   1.202, 2.607, 882,
                      2.171, 0]]


def funcao_objetivo(solucao):
    distancia = 0
    for i in range(0, len(solucao) - 1):
        distancia = distancia + matriz_distancias[solucao[i]][solucao[i + 1]]
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
            print("Metodo Guloso")
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
            print("Metodo Aleatório")
            indice = randrange(len(cidades_copia))
            cidade_sorteada = cidades_copia[indice]
            del cidades_copia[indice]
            solucao.append(cidade_sorteada)

    print("Solução final :", solucao, " Distancia = ", funcao_objetivo(solucao))
