from pyvis.network import Network
import networkx as nx
import matplotlib.pyplot as plt

from script.github_export import get_repository_tree, format_tree_df

color_of_extension = {
    "py" : "#3572A5",
    "js" : "#f1e05a",
    "css" : "#563d7c",
    "html" : "#e34c26",
    "json" : "#292929",
    "folder" : "dark-grey",
}

def create_network_graph(df_graph_tree):
    """Create a Network from the database of nodes and edges"""
    net = Network(height='750px', width='100%', directed=True)
    net.force_atlas_2based()
    for index, row in df_graph_tree.iterrows():
        src = row['Source']
        dst = row['Target']
        label = row['Label']
        title = "File fullname : {} <br> Type : {}".format(row['Source'], row['File Type'])
        color = color_of_extension[row['File Type']] if row['File Type'] in color_of_extension.keys() else 'grey'
        net.add_node(src, label=label, color = color, title = title)
        if dst != '':
            net.add_node(dst, label=label, )
            net.add_edge(src, dst, value=1, color = '#ADD8E6')
    return net
    