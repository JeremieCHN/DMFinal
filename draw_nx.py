"""
用NetworkX进行画图
"""

import networkx as nx
import matplotlib.pyplot as plt
import random
import file_io

def read_graph(data_dir):
    '读取点集和边集'
    nodes = []
    nodes_file = open(data_dir + '\\nodes.csv', 'r')
    for line in nodes_file:
        nodes.append(line[0:-1])
    nodes_file.close()

    edges = []
    edges_file = open(data_dir + '\\edges.csv', 'r')
    for line in edges_file:
        uv = line[0:-1].split(',')
        edges.append((uv[0], uv[1]))
    edges_file.close()
    return nodes, edges

def get_colors(count):
    '随机颜色'
    colors = set()
    while len(colors) < count:
        colors.add((random.uniform(0,1),random.uniform(0,1),random.uniform(0,1)))
    return list(colors)

def main(data_dir):
    '主函数'
    nodes, edges = read_graph(data_dir)
    communities = file_io.read_communities(data_dir)
    nodes = []
    for community in communities:
        nodes += community
    graph = nx.Graph()
    graph.add_nodes_from(nodes)
    graph.add_edges_from(edges)

    colors = get_colors(len(communities))
    position = nx.circular_layout(graph)
    for i in range(len(communities)):
        nx.draw_networkx_nodes(graph, position, nodelist=communities[i], node_color=[colors[i]])
    nx.draw_networkx_edges(graph, position)
    nx.draw_networkx_labels(graph, position)
    plt.show()

if __name__ == "__main__":
    # main('D:\\1.MyFiles\\11.非全\\数据挖掘\\DMFinal\\Data\\dolphins')
    # main('D:\\1.MyFiles\\11.非全\\数据挖掘\\DMFinal\\Data\\football')
    # main('D:\\1.MyFiles\\11.非全\\数据挖掘\\DMFinal\\Data\\karate')
    main('D:\\1.MyFiles\\11.非全\\数据挖掘\\DMFinal\\Data\\simple')
