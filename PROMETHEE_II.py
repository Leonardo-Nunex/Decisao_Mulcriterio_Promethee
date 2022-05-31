
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
    print('-------------------------------------------------------------------------------------------------------------------')
    print('-----------------------------------MÉTODO MULTICRITÉRIO: PROMETHEE II----------------------------------------------')
    print('-------------------------------------------------------------------------------------------------------------------')

    print('O Metodo será realizado seguindo as etapas a seguir?')
    
    print('1º Definição da Matriz de performance de ação')
    print('2º Definição da Matriz de performance de ação')
    print('3º Definição da Matriz de performance de ação')
    print('4º Definição da Matriz de performance de ação')
    print('5º Definição da Matriz de performance de ação')
    print('6º Definição da Matriz de performance de ação')

    Alternativas = int (input( "Quantas alternativas serão avaliadas ?")) # necessário desenvolver logica
    Criterios = int (input( "Quantos critérios serão considerados ?")) # necessário desenvolver logica

    # matriz de performances de ação - action performances array

    MX1 = []
    Posicao = 0
    for i in range(4):
        Posicao = Posicao + 1
        print('Alternativa 1 - Insira o',Posicao,'º dados dos critérios:')
        Elemento = int (input())
        MX1.append(Elemento)
    print("Matriz de Ação - Alternativa 1 = ", MX1)
        

    MX2 = []
    Posicao = 0
    for i in range(5):
        Posicao = Posicao + 1
        Elemento = int (input('Alternativa 2 - Insira o',Posicao,'º dados dos critérios:'))
        MX2.append(Elemento)

    print("Matriz de Ação - Alternativa 2 = ", MX2) 

    MX3 = []
    Posicao = 0
    for i in range(4):
        Posicao = Posicao + 1
        Elemento = int (input('Alternativa 3 - Insira o',Posicao,'º dados dos critérios:'))
        MX3.append(Elemento)

    print("Matriz de Ação - Alternativa 3 = ", MX3) 

    MX4 = []
    Posicao = 0
    for i in range(4):
        Posicao = Posicao + 1
        Elemento = int (input('Alternativa 4 - Insira o',Posicao,'º dados dos critérios:'))
        MX4.append(Elemento)

    print("Matriz de Ação - Alternativa 4 = ", MX4) 

    MX5 = []
    Posicao = 0
    for i in range(4):
        Posicao = Posicao + 1
        Elemento = int (input('Alternativa 5 - Insira o',Posicao,'º dados dos critérios:'))
        MX5.append(Elemento)

    print("Matriz de Ação - Alternativa 5 = ", MX5) 

    MX6 = []
    Posicao = 0
    for i in range(4):
        Posicao = Posicao + 1
        Elemento = int (input('Alternativa 6 - Insira o',Posicao,'º dados dos critérios:'))
        MX6.append(Elemento)

    print("Matriz de Ação - Alternativa 6 = ", MX6) 


    x = array([MX1, MX2, MX3, MX6]) #[4, 3, 8, 8] ,[3, 1, 5, 2],[2, 3, 5, 3],[1, 5, 7, 4], [1, 2, 3, 1], [2, 3, 6, 5]
            

    # parâmetros de preferência de toda a matriz de critérios - preference parameters of all criteria array
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
