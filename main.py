import networkx as nx
import time
import file_io

def load_data(data_dir):
    '读取csv文件'
    graph = nx.Graph()

    nodes = file_io.read_nodes(data_dir)
    graph.add_nodes_from(nodes)

    edges = file_io.read_edges(data_dir)
    graph.add_edges_from(edges)
    return graph

def calc_betweenness(graph):
    '计算介值'
    betweenness = dict()
    for edge in graph.edges:
        betweenness[edge] = 0
    paths = nx.shortest_path(graph)
    nodes = list(graph.nodes)
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            if nodes[i] not in paths or nodes[j] not in paths[nodes[i]]:
                continue
            path = paths[nodes[i]][nodes[j]]
            for k in range(len(path) - 1):
                edge = (path[k], path[k+1])
                if edge not in betweenness:
                    edge = (path[k+1], path[k])
                betweenness[edge] += 1
    return betweenness

def get_max_betweenness_edges(betweenness):
    '介值最大的边的集合'
    betweenness = list(betweenness.items())
    betweenness.sort(key=lambda x: x[1], reverse=True)
    max_betweenness_edges = []
    for i in range(len(betweenness)):
        if betweenness[i][1] == betweenness[0][1]:
            max_betweenness_edges.append(betweenness[i][0])
        else:
            break
    return max_betweenness_edges


def calc_modularity(graph, connections):
    '计算目标函数的值'
    Q = 0
    m = len(graph.edges)
    for sub_nodes in connections:
        sub_nodes = list(sub_nodes)
        for i in range(len(sub_nodes)):
            for j in range(i+1, len(sub_nodes)):
                ki = graph.degree[sub_nodes[i]]
                kj = graph.degree[sub_nodes[j]]
                if graph.has_edge(sub_nodes[i], sub_nodes[j]):
                    Aij = 1
                else:
                    Aij = 0
                Q += Aij - ki * kj / (2 * m)
    return Q / (2 * m)

def main(data_dir):
    '主函数'
    graph = load_data(data_dir)
    max_modularity = 0
    max_subgraphs = None
    file_betweenness = open(data_dir + '\\recode.txt', 'w')

    try:
        while True:
            betweenness = calc_betweenness(graph) # 计算介值
            max_betweenness_edges = get_max_betweenness_edges(betweenness) # 获取介值最大的边
            # 去掉介值最大的边
            for (u, v) in max_betweenness_edges:
                if (u, v) in graph.edges:
                    graph.remove_edge(u, v)
                elif (v, u) in graph.edges:
                    graph.remove_edge(v, u)
            if len(graph.edges) == 0:
                break
            connections = list(nx.connected_components(graph)) # 获取连通分量，也就是当前分出来的社区
            modularity = calc_modularity(graph, connections) # 计算目标函数，寻找最高点
            file_betweenness.write(str(modularity) + '\n') # 当前的目标值写入文件以便后续解析
            if (modularity > max_modularity):
                max_modularity = modularity
                max_subgraphs = connections
                file_io.write_communities(data_dir, max_subgraphs)
    except Exception as err:
        print(err)
    finally:
        file_betweenness.close()
        file_io.write_communities(data_dir, max_subgraphs)

if __name__ == "__main__":
    start = time.time()
    main('D:\\1.MyFiles\\11.非全\\数据挖掘\\DMFinal\\Data\\dolphins')
    # main('D:\\1.MyFiles\\11.非全\\数据挖掘\\DMFinal\\Data\\football')
    # main('D:\\1.MyFiles\\11.非全\\数据挖掘\\DMFinal\\Data\\karate')
    # main('D:\\1.MyFiles\\11.非全\\数据挖掘\\DMFinal\\Data\\simple')
    print('Finish', time.time() - start)
