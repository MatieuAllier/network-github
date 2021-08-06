import streamlit as st
import streamlit.components.v1 as components

from script.network_graph import create_network_graph
from script.github_export import get_repository_tree, format_tree_df

rep_name = st.sidebar.text_input('Github Repository Name :', value='octocat/octocat.github.io')
branch_name = st.sidebar.text_input('Branch Name :', value='master')
if st.sidebar.button('Create Graph'):
    if len(rep_name.split('/')) != 2:
        st.text('This is not a valid Repository Name.')
    else:
        owner = rep_name.split('/')[0]
        rep = rep_name.split('/')[1]
        try:
            tree_data = get_repository_tree(owner, rep, branch)
            df_graph_tree = format_tree_df(tree_data)
            net = create_network_graph(df_graph_tree)
            # Need to save the graph in html to read it in streamlit
            net.save_graph('graph.html')
            HtmlFile = open("graph.html", 'r', encoding='utf-8')
            source_code = HtmlFile.read() 
            components.html(source_code, height = 900,width=900)
        except:
            st.text('This is not a valid Repository Name.')