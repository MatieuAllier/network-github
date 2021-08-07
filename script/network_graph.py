from pyvis.network import Network
import networkx as nx
import matplotlib.pyplot as plt
import json

from script.github_export import get_repository_tree, format_tree_df

f = open('./ressources/colors.json')
color_of_extension = json.load(f)

# color_of_extension = {
#     "py" : "#3572A5",
#     "js" : "#f1e05a",
#     "css" : "#563d7c",
#     "html" : "#e34c26",
#     "json" : "#292929",
#     "folder" : "light grey",
#     "r" : "#198CE7",
#     "rd" : "#198CE7",
# }

def create_network_graph(df_graph_tree):
    """Create a Network from the database of nodes and edges"""
    net = Network(height='750px', width='100%', directed=True, bgcolor='#222222', font_color='white')
    net.force_atlas_2based(gravity=-75)
    for index, row in df_graph_tree.iterrows():
        src = row['Source']
        dst = row['Target']
        label = row['Label']
        title = "File fullname : {} <br> Type : {}".format(row['Source'], row['File Type'])
        color = color_of_extension[row['File Type'].lower()] if row['File Type'].lower() in color_of_extension.keys() else 'grey'
        if row['File Type'] == 'folder':
            net.add_node(src, shape='text', label=label, color = color, title = title)
        else:
            net.add_node(src, shape='dot', label=label, color = color, title = title)
        if dst != '':
            #net.add_node(dst, label=label, title=title)
            net.add_edge(src, dst, value=1, color = '#d3d3d3')
    return net
    