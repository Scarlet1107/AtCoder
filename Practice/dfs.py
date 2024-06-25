import networkx as nx

# グラフの定義
G = nx.Graph()
edges = [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (4, 5)]
G.add_edges_from(edges)

# 頂点連結度を求める
k = nx.node_connectivity(G)

# 結果の表示
print(f"The k-connectivity of the graph is: {k}")
