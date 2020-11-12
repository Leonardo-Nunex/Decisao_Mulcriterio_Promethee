

import matplotlib.pyplot as plt
from numpy import *
from PROMETHEE_Preference_Functions import uni_cal
from PROMETHEE_Final_Rank_Figure import graph, plot

# PROMETHEE method: método: chama as outras funções
def promethee(x, p, c, d, w):
    """ x é o conjunto de desempenhos de ação, b é o
    matriz com os parâmetros de preferência de todos
    critérios, c é o critério min (0) ou max (1)
    matriz de otimização, d é a preferência
    matriz de funções ('u' para habitual, 'us' para
    forma de u, 'vs' para forma de v, 'le' para nível,
    'li' para linear e 'g' para gaussiano) e w é a matriz de pesos
    """
    weighted_uni_net_flows = []
    total_net_flows = []
    for i in range(x.shape[1]):
        weighted_uni_net_flows.append(w[i] *
            uni_cal(x[:, i:i + 1], p[:,
            i:i + 1], c[i], d[i]))

    # print the weighted unicriterion preference
    # net flows
    for i in range(size(weighted_uni_net_flows, 1)):
        k = 0
        for j in range(size(weighted_uni_net_flows, 0)):
            k = k + round(weighted_uni_net_flows[j][i], 5)
        total_net_flows.append(k)
    return around(total_net_flows, decimals = 4)

# função principal
def main(a, b):
    """ a e b são bandeiras; se eles estão definidos para 'y', eles fazem
    imprimir os resultados, qualquer outra coisa não imprime
    os resultados
	"""

    # action performances array
    x = array([[4, 3, 8, 8], [3, 1, 5, 2], [2, 3, 5, 3],
        [1, 5, 7, 4], [1, 2, 3, 1], [2, 3, 6, 5]])

    # preference parameters of all criteria array
    p = array([[1, 1, 1, 1], [2, 2, 2, 2]])

    # criteria min (0) or max (1) optimization array
    c = ([1, 1, 1, 1])

    # preference function array
    d = (['li', 'li', 'li', 'li'])

    # weights of criteria
    w = array([0.4, 0.4, 0.1, 0.1])

    # final results
    final_net_flows = promethee(x, p, c, d, w)
    print("Global preference flows = ", final_net_flows)
    if a == 'y':
        graph(final_net_flows, "Phi")
    if b == 'y':
        plot(final_net_flows, "PROMETHEE II")
    return final_net_flows

if __name__ == '__main__':
    main('n','y')
