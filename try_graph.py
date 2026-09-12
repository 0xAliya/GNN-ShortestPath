"""第一个图脚本：用 NetworkX 建图、加权重、查邻居、可视化。

学习目标：
1. 图 = 节点 + 边，边可以带权重；
2. G.edges() 遍历边、G.neighbors(n) 查邻居、G[u][v] 访问边属性；
3. spring_layout 给节点算坐标，nx.draw 负责画。
"""

import random

import matplotlib.pyplot as plt
import networkx as nx

# TODO 1: 建一个 5 节点的图，节点用 0-4 编号
G = nx.Graph()
G.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 4), (0, 4), (1, 3)])

# TODO 2: 给每条边加一个随机权重（0.1 ~ 1.0）
# uniform(a, b) 返回 [a, b] 区间的小数——权重应该是小数，不是整数
for u, v in G.edges():
    G[u][v]["weight"] = round(random.uniform(0.1, 1.0), 2)

# TODO 3: 打印节点数、边数、节点 0 的邻居列表
# 注意：G.neighbors(0) 返回的是迭代器，不打印内容，要用 list() 转换
print(f"节点数: {G.number_of_nodes()}")
print(f"边数: {G.number_of_edges()}")
print(f"节点 0 的邻居: {list(G.neighbors(0))}")

# 打印每条边及其权重（检查权重是否写进去了）
for u, v, d in G.edges(data=True):
    print(f"边 ({u}, {v}) 权重 = {d['weight']}")

# TODO 4: 画图并保存为 try_graph.png
# spring_layout: 力导向布局，把节点摆成好看的位置
pos = nx.spring_layout(G, seed=42)  # seed 固定布局，每次运行图形一样
nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=700, font_weight="bold")

# 把权重标在边上
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.savefig("try_graph.png", dpi=150, bbox_inches="tight")
print("已保存 try_graph.png")
