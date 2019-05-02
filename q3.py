import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import time
import sys



def WPGMA(matrixFile):
    b = []
    counter = 0
    start = time.time()
    with open(matrixFile) as infile:
        lines = infile.readlines()
        for line in lines:
            b.append([])
            for n in line.split():
                b[counter].append(n)
            counter += 1
    G = nx.Graph()
    print(np.array(b))
    while len(b) > 3:
        lst = []
        coords = []
        for i in range(1, len(b)):
            for j in range(1, i):
                lst.append(float(b[j][i]))
                coords.append([j,i])
        index = coords[lst.index(min(lst))]
        node0 = b[0][index[0]]
        node1 = b[0][index[1]]
        b[index[0]][index[1]] = '0'
        b[index[1]][index[0]] = '0'
        if node0 not in G.nodes():
            G.add_node(node0)
        if node1 not in G.nodes():
            G.add_node(node1)
        for i in range(1, len(b)):
            b[index[0]][i] = str((float(b[index[0]][i]) + float(b[index[1]][i]))/2)
            b[i][index[0]] = b[index[0]][i]
        b[0][index[0]] = b[0][index[0]] + b[0][index[1]]
        b[index[0]][0] = b[0][index[0]]
        b[index[0]][index[1]] = '0'
        b.remove(b[index[1]])
        for row in b:
            row.remove(row[index[1]])
        G.add_node(b[0][index[0]])
        G.add_edge(b[0][index[0]], node0)
        G.add_edge(b[0][index[0]], node1)
        c = np.array(b)
        print(c)
        node0 = b[0][1]
        node1 = b[0][2]
        if node0 not in G.nodes():
            G.add_node(node0)
        if node1 not in G.nodes():
            G.add_node(node1)
        node2 = node0 + node1
    G.add_node(node2)
    G.add_edge(node0, node2)
    G.add_edge(node1, node2)
    nx.draw(G, with_labels = True)
    #plt.show()
    plt.savefig('tree.png')
    end = time.time() - start
    print(end)


file = sys.argv[1]
WPGMA(file)

        


    
