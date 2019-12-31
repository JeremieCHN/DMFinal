from graphviz import Graph
import file_io
import random


def get_colors(count):
    '随机颜色'
    colors = set()
    while len(colors) < count:
        colors.add((random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)))
    hex_colors = []
    for color in colors:
        color_str = '#'
        for i in color:
            i = hex(i)[2:]
            if len(i) != 2:
                i = '0' + i
            color_str += i
        hex_colors.append(color_str)
    return hex_colors

def main(data_dir: str):
    nodes = file_io.read_nodes(data_dir)
    edges = file_io.read_edges(data_dir)
    groups = file_io.read_communities(data_dir)

    graph = Graph()
    for node in nodes:
        graph.node(node)
    graph.edges(edges)

    colors = get_colors(len(groups))
    for i in range(len(groups)):
        group = groups[i]
        color = colors[i]
        with graph.subgraph(name='cluster-'+str(i)) as subgraph:
            subgraph.attr(color=color)
            for node in group:
                subgraph.node(node, color=color, style='filled')

    graph.format = 'png'
    graph.render(data_dir+'\\graph.gv')
    graph.view()

if __name__ == "__main__":
    # main('D:\\1.MyFiles\\11.非全\\数据挖掘\\DMFinal\\Data\\dolphins')
    # main('D:\\1.MyFiles\\11.非全\\数据挖掘\\DMFinal\\Data\\football')
    # main('D:\\1.MyFiles\\11.非全\\数据挖掘\\DMFinal\\Data\\karate')
    main('D:\\1.MyFiles\\11.非全\\数据挖掘\\DMFinal\\Data\\simple')
