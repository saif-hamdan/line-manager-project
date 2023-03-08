from typing import List
import networkx as nx
import matplotlib
matplotlib.use('WebAgg')
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout
from src.container import Container  



def show_graph(tree:List[Container]):
    
    G = nx.MultiDiGraph()

    for item in tree:
        if item.parentContainer is not None:
        
            G.add_node(item.containerName)


    for item in tree:
        if item.parentContainer is not None:
            
            for child in item.childContainers:
                G.add_edge(item.containerName, child.containerName)
            
            
            
    
    
    plt.figure(1,figsize=(52,15)) 
    G = nx.MultiDiGraph.reverse(G)

    nx.draw(G,graphviz_layout(G),with_labels=True,font_size=7,margins=0.04,node_size=8200,arrowsize=15,node_shape='8',node_color='#eab676',bbox=dict(facecolor='#eab676',linewidth=0))


    plt.show() 
    
    input()