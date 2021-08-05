# %%
import requests
from pandas.io.json import json_normalize
import networkx as nx
import matplotlib.pyplot as plt
import collections.abc

def update(d, u):
    for k, v in u.items():
        if isinstance(v, collections.abc.Mapping):
            d[k] = update(d.get(k, {}), v)
        else:
            d[k] = v
    return d

# %%

def get_repository_tree(owner, rep, branch="master"):
    """
    Returns the tree of a github repository.
    Args:
        - owner : github name of the repository owner
        - rep : repository name
        - branch : branch you want to export
    Returns :
        - list of dicitonnary of the different element of the repository
    """
    url = "https://api.github.com/repos/{}/{}/git/trees/{}?recursive=1".format(
        owner,
        rep,
        branch
    )
    r = requests.get(url=url)
    try:
        tree_data = r.json()["tree"]
    except Exception:
        raise ValueError("Error in the API Call check your parameter")
    return tree_data

def format_tree(tree_data):
    """Format the output of the get_repository function."""
    dict_ordoned_tree = {}
    for element in tree_data:
        splits = element['path'].split('/')
        if len(splits) > 1:
            dict_path = {''.join(splits[:-1]) : {element['path'] : element['path']}}
        else:
            dict_path = {element['path'] : {}}
        dict_ordoned_tree = update(dict_ordoned_tree, dict_path)
    return dict_ordoned_tree

        
        

if __name__ =="__main__":
    owner = "octocat"
    rep = "octocat.github.io"
    branch = "master"
    tree_data = get_repository_tree(owner, rep, branch="master")
    dict_graph_tree = format_tree(tree_data)
    #d = {0: {1: {2 : 2}}}
    G = nx.DiGraph(dict_graph_tree)
    subax1 = plt.subplot(121)
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()
    print(dict_graph_tree)
