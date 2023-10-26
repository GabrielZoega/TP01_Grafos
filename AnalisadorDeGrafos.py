import matplotlib.pyplot as plt
import networkx as nx
import os

def adicionaPesos(G, arquivo):
    graphml = open(arquivo, "r")
   
    linha = graphml.readline()     
    teste = linha.split("><")
    
    for i in range(len(teste)):
        
        if teste[i].find("edge ") != -1:
            peso = ""
            source = ""
            target = ""
            sourceIndice  = teste[i].find("source") + 8
            targetIndice = teste[i].find("target") + 8
            pesoIndice = teste[i].find("weight") + 8

            while(teste[i][sourceIndice] != '"'):
                source += teste[i][sourceIndice]
                sourceIndice = sourceIndice + 1
                
            while(teste[i][targetIndice] != '"'):
                target += teste[i][targetIndice]
                targetIndice = targetIndice + 1    

            while(teste[i][pesoIndice] != '"'):
                peso += teste[i][pesoIndice]
                pesoIndice = pesoIndice + 1

            G.add_edge(source, target, weight = float(peso))
    graphml.close()
    return

def ordem(grafo):
    ordem = grafo.number_of_nodes()
    return ordem

def tamanho(grafo):
    tamanho = grafo.number_of_edges()
    return tamanho

def vizinhos(grafo, vertice):
    vizinhos = list(grafo.adj[vertice])
    return vizinhos

def grau(grafo, vertice):
    grau = grafo.degree[vertice]
    return grau

def sequenciaGraus(grafo):
    listaDeGraus = []
    for i in range(ordem(grafo)):
        listaDeGraus.append(grau(grafo = grafo, vertice = str(i)))
        listaDeGraus.sort(reverse = True)
    return listaDeGraus

def distancia(grafo, vertice1, vertice2):
    
    try:
        menorcaminho = nx.shortest_path(grafo, source = vertice1, target = vertice2, weight = 'weight')
        menorcaminho = nx.path_weight(G = grafo, path = menorcaminho, weight = "weight")
        return menorcaminho
    except:
        return "infinita"

def excentricidade(grafo, vertice):
    try:
        excent = nx.eccentricity(grafo, v = vertice, weight = 'weight')
        return excent
    except:
        return "infinita"

def descobreTodasExcentricidades(grafo):
    x = []
    for i in range (ordem(grafo)):
        x.append(excentricidade(grafo, str(i)))
    return x
        
def raio2(grafo):
    try:
        return nx.radius(G = grafo, weight = "weight")
    except:
        return "infinito"

def diametro2(grafo):
    try:
        return nx.diameter(grafo, weight = "weight")
    except:
        return "infinito"

def centro2(grafo):
    try:
        return list(nx.center(G = grafo, weight = "weight"))
    except:
        return "Considerando que todos os raios sao infinitos, todos os vertices fazem parte do centro\n" + str(nx.nodes(grafo))      #Perguntar se são todos os vértices

def menorCaminho(grafo, vertice):
    return nx.shortest_path(grafo, source = vertice, weight = "weight")

def buscaEmLargura(grafo, vertice):
    return nx.bfs_tree(grafo, source = vertice)

def arestasRemovidas(grafo, arvore):
    arestas = []
    arestasGrafo = nx.generate_edgelist(G = grafo)    
    arestasArvore = nx.generate_edgelist(G = arvore)
   
    for arestaGrafo in arestasGrafo:
        arestasArvore = nx.generate_edgelist(G = arvore)
        achou = 0
        for arestaArvore in arestasArvore:
            if arestasSaoIguais(arestaGrafo, arestaArvore) == True:
                achou += 1
        if achou == 0:
            arestas.append(arestaGrafo[0:3])
    return arestas

def arestasSaoIguais(i, j):
    return ((i[0] == j[0] and i[2] == j[2]) or (i[0] == j[2] and i[2] == j[0]))

def centralidade (grafo, vertice):
    nVertices = ordem(grafo)
    soma = 0
    cent = 0
    for i in range(nVertices):
        if (distancia(grafo, vertice, str(i)) != "infinita"):
            soma += distancia(grafo, vertice, str(i))
    cent = (nVertices - 1)/soma
    return cent

def pegaVertices(vet):
    caractere = caractere = "[],' "
    for i in range(0, len(caractere)):
            vet = vet.replace(caractere[i], "")
    return vet

def pegaDiferentes(vet1, vet2):
    
    for i in range(0, len(vet2)):
        vet1 = vet1.replace(vet2[i], "")
    
    return vet1

controleMenu = 1
caminhoGrafo = str(input("Digite o caminho do seu Grafo: "))
grafo = nx.read_graphml(path = caminhoGrafo)
adicionaPesos(grafo, caminhoGrafo)




while controleMenu == 1:    
    print("Selecione a atividade que deseja fazer com o grafo:")
    print(" 1- Ordem\n 2- Tamanho\n 3- Vizinhos de um vertice fornecido\n 4- Grau de um vertice fornecido")
    print(" 5- Sequencia de graus do grafo\n 6- Distancia entre dois vertices\n 7- Menor caminho de um vertice fornecido")
    print(" 8- Excentricidade de um vertice fornecido\n 9- Raio\n10- Diametro\n11- Centro\n12- Busca em largura\n13- Centralidade")
   
    menu = int(input("Opcao escolhida: "))
    if menu == 1:
        print("\n\tOrdem: " + str(ordem(grafo)) + "\n")

    elif menu == 2:
        print("\n\tTamanho: " + str(tamanho(grafo)) + "\n")
   
    elif menu == 3: 
        n = int(input("\n\tCom qual vertice deseja trabalhar?"))
        print("\tVizinhos: " + str(vizinhos(grafo,str(n))) + "\n")
   
    elif menu == 4: 
        n = int(input("\n\tCom qual vertice deseja trabalhar?"))
        print("\tGrau do vertice: " + str(grau(grafo,str(n))) + "\n")
   
    elif menu == 5:
        print("\n\tSequencia de graus: " + str(sequenciaGraus(grafo)) + "\n")
   
    elif menu == 6:
        print("\n\tCom quais vertices deseja trabalhar?")
        n = input("\tVertice 01:")
        m = input("\tVertice 02:")
        print("\tDistancia: " + str(distancia(grafo,n, m)) + "\n")
   
    elif menu == 7:
        n = int(input("\n\tCom qual vertice deseja trabalhar:"))
        print("\tMenor caminho: " + str(menorCaminho(grafo,str(n))) + "\n")
   
    elif menu == 8:
        n = int(input("\n\tCom qual vertice deseja trabalhar:"))
        print("\tExcentricidade: " + str(excentricidade(grafo,str(n))) + "\n")

   
    elif menu == 9:
        print("\n\tRaio: " + str(raio2(grafo)) + "\n") 
   
    elif menu == 10:
        print("\n\tDiametro: " + str(diametro2(grafo)) + "\n")
   
    elif menu == 11:
        print("\n\tCentro: " + str(centro2(grafo)) + "\n")
   
   
    elif menu == 12:
        n = int(input("\n\tA partir de qual vertice deseja fazer a busca? "))
        arvore = buscaEmLargura(grafo, str(n))
        vetorUsados = []
        
        if(nx.is_forest(arvore)):
            
            diferentes = pegaDiferentes((pegaVertices(str(nx.nodes(grafo)))), (pegaVertices(str(nx.nodes(arvore)))))
            i = 0
            
            while diferentes != "":
                
                disconexo = buscaEmLargura(grafo, diferentes[0])
                composicao = nx.compose(arvore, disconexo)
                nx.write_graphml_xml(composicao, 'arvoreTeste.graphml')
                diferentes = pegaDiferentes((pegaVertices(str(nx.nodes(grafo)))), (pegaVertices(str(nx.nodes(composicao)))))
                
                arvore = composicao
             
            print("\tArestas faltantes: " + str(arestasRemovidas(grafo, composicao)) + "\n")
            print("\tSequeência de Vértices Visitados: " + str(nx.nodes(composicao)))
            nx.draw(composicao, with_labels=True, font_weight='bold')
            plt.show()
            
        else:
            nx.write_graphml_xml(arvore, 'arvoreTeste.graphml')
            print("\tArestas faltantes: " + str(arestasRemovidas(grafo, arvore)) + "\n")
            nx.draw(arvore, with_labels=True, font_weight='bold')
            plt.show()
             
             
    elif menu == 13:
        n = int(input("\n\tCom qual vertice deseja trabalhar?"))
        print("\tCentralidade do vertice: " + str(centralidade(grafo,str(n))) + "\n")
        
    option = int (input("Deseja imprimir o seu grafo na tela? \n 0: Nao \n 1: Sim \n"))
    if option == 1:
        nx.draw(grafo, with_labels=True, font_weight='bold')
        plt.show()
    
    controleMenu = int(input("Deseja testar outra funcao? \n0: Nao \n1: Sim \n"))
    os.system('clear')