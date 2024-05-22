import uuid
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

class Node:
    def __init__(self, key, color="#000000"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  
        self.id = str(uuid.uuid4())  

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  

    plt.figure(figsize=(10, 7))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def array_to_bst(arr, index=0):
    if index >= len(arr):
        return None
    root = Node(arr[index])
    root.left = array_to_bst(arr, 2 * index + 1)
    root.right = array_to_bst(arr, 2 * index + 2)
    return root

def color_nodes_by_traversal(tree_root, traversal_order):
    colors = list(mcolors.TABLEAU_COLORS.values())
    color_step = len(colors) // len(traversal_order)
    
    for i, node in enumerate(traversal_order):
        node.color = colors[(i * color_step) % len(colors)]

def dfs_traversal(node, order):
    if node:
        order.append(node)
        dfs_traversal(node.left, order)
        dfs_traversal(node.right, order)

def bfs_traversal(node):
    order = []
    queue = [node]
    while queue:
        current = queue.pop(0)
        if current:
            order.append(current)
            queue.append(current.left)
            queue.append(current.right)
    return order

def main():

    heap_array = [0, 4, 1, 5, 10, 3]


    heap_tree = array_to_bst(heap_array)

    #  (DFS)
    dfs_order = []
    dfs_traversal(heap_tree, dfs_order)
    color_nodes_by_traversal(heap_tree, dfs_order)
    print("Візуалізація обходу в глибину (DFS):")
    draw_tree(heap_tree)

  
    heap_tree = array_to_bst(heap_array)

    #  (BFS)
    bfs_order = bfs_traversal(heap_tree)
    color_nodes_by_traversal(heap_tree, bfs_order)
    print("Візуалізація обходу в ширину (BFS):")
    draw_tree(heap_tree)

if __name__ == "__main__":
    main()
