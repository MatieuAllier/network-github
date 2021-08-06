from pyvis.network import Network
import networkx as nx
import matplotlib.pyplot as plt

from github_export import get_repository_tree, format_tree_df

def add_nodes_pyvis(g, dict_graph_tree):
    nodes = list(dict_graph_tree.keys())
    nodes += []
    print(nodes)
    nodes_labels = nodes

if __name__ == '__main__':
    owner = "octocat"
    rep = "octocat.github.io"
    branch = "master"
    tree_data = get_repository_tree(owner, rep, branch="master")
    df_graph_tree = format_tree_df(tree_data)
    net = Network(height='750px', width='100%')
    net.barnes_hut()
    for index, row in df_graph_tree.iterrows():
        src = row['Source']
        dst = row['Target']
        label = row['Label']
        print(label)
        net.add_node(src, label=label)
        if dst != '':
            net.add_node(dst, label=label)
            net.add_edge(src, dst, value=1)
    # set the physics layout of the network
    
    net.show('test.html')