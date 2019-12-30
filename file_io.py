"""
文件读写
"""

def read_nodes(data_dir):
    '读取点文件'
    nodes = []
    nodes_file = open(data_dir + '\\nodes.csv', 'r')
    for line in nodes_file:
        nodes.append(line[0:-1])
    nodes_file.close()
    return nodes

def read_edges(data_dir):
    '读取边文件'
    edges = []
    edges_file = open(data_dir + '\\edges.csv', 'r')
    for line in edges_file:
        uv = line[0:-1].split(',')
        edges.append(tuple(uv))
    edges_file.close()
    return edges

def write_communities(dir, communities):
    '写入社区'
    out_file = open(dir + '\\result.txt', 'w')
    for community in communities:
        for node in community:
            out_file.write(str(node) + ',')
        out_file.seek(out_file.tell() - 1)
        out_file.write('\n')
    out_file.close()

def read_communities(data_dir):
    '读取社区'
    communities = []
    communities_file = open(data_dir + '\\result.txt', 'r')
    for line in communities_file:
        communities.append(line[0:-1].split(','))
    communities_file.close()
    return communities
