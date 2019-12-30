def main(data_dir):
    group_file = open(data_dir + '\\result.txt')
    groups = dict()
    group_index = 1
    for line in group_file:
        group = line[0:-1].split(',')
        for node in group:
            groups[node] = group_index
        group_index += 1
    group_file.close()

    gml = open(data_dir + '\\graph.gml', 'w')
    gml.write('graph')
    gml.write('[\n')
    gml.write('  directed 0\n')
    # 写入点
    nodes_file = open(data_dir + '\\nodes.csv')
    for line in nodes_file:
        node = line[0:-1]
        gml.write('  node\n')
        gml.write('  [\n')
        gml.write('    id ' + node + '\n')
        gml.write('    label \"' + node + '\"\n')
        gml.write('  ]\n')
    nodes_file.close()
    # 写入边
    edges_file = open(data_dir + '\\edges.csv')
    for line in edges_file:
        edge = line[0:-1].split(',')
        gml.write('  edge\n')
        gml.write('  [\n')
        gml.write('    source ' + edge[0] + '\n')
        gml.write('    target ' + edge[1] + '\n')
        gml.write('  ]\n')
    edges_file.close()

    gml.write(']\n')
    gml.close()

if __name__ == "__main__":
    main('D:\\1.MyFiles\\11.非全\\数据挖掘\\DMFinal\\Data\\dolphins')
    # main('D:\\1.MyFiles\\11.非全\\数据挖掘\\DMFinal\\Data\\football')
    # main('D:\\1.MyFiles\\11.非全\\数据挖掘\\DMFinal\\Data\\karate')
    # main('D:\\1.MyFiles\\11.非全\\数据挖掘\\DMFinal\\Data\\simple')
