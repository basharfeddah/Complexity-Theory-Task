import networkx as nx
import time
#حنين نزيه بدور
def strongly_connected_components(graph):
    """
    Cheriyan-Mehlhorn-Gabow algorithm for finding strongly connected components.
    Using NetworkX's built-in function, which implements Tarjan's algorithm (similar complexity).
    """
    scc = list(nx.strongly_connected_components(graph))
    return scc
#حنين رمضان احمد
def is_2_connected(graph):
    """
    Jens Schmidt's algorithm for testing whether an undirected graph is 2-connected.
    """
    undirected_graph = graph.to_undirected()
    articulation_points = list(nx.articulation_points(undirected_graph))
    return len(articulation_points) == 0
#رهف رفيق الحكيم
def is_2_vertex_strongly_biconnected(graph):
    """
    Test whether a directed graph is 2-vertex strongly biconnected.
    """
    # Check if the graph has at least three vertices
    if len(graph) < 3:
        return False

    # Check if the graph is strongly connected
    if not nx.is_strongly_connected(graph):
        return False
#سالي محمد ابراهيم
    # Check if G{w} is strongly connected for all vertices w in G
    for node in list(graph.nodes):
        temp_graph = graph.copy()
        temp_graph.remove_node(node)
        if not nx.is_strongly_connected(temp_graph):
            return False

    return True
#بشار نبيل فضه
def load_graph_from_edge_list(file_path):
    """
    Load a graph from an edge list file.
    """
    graph = nx.DiGraph()
    with open(file_path, 'r') as f:
        for line in f:
            src, dst = map(int, line.strip().split())
            graph.add_edge(src, dst)
    return graph

def main():
    # Path to your graph file
    file_path = r'C:\Users\basharfeddah\PycharmProjects\pythonProject\data-sets\facebook_combined.txt'  # Update with your actual path

    # Load the graph from the edge list
    nx_graph = load_graph_from_edge_list(file_path)

    # Step 1: Find strongly connected components
    start_time = time.time()
    scc = strongly_connected_components(nx_graph)
    end_time = time.time()
    print(f"Strongly connected components found in {end_time - start_time:.6f} seconds.")
#رند احمد شعبان
    # Step 2: Check if the undirected graph is 2-connected
    start_time = time.time()
    is_2_conn = is_2_connected(nx_graph)
    end_time = time.time()
    print(f"Undirected graph is 2-connected: {is_2_conn} (checked in {end_time - start_time:.6f} seconds).")
#رغد كارم محمد
    # Step 3: Check if the graph is 2-vertex strongly biconnected
    start_time = time.time()
    is_2_vsb = is_2_vertex_strongly_biconnected(nx_graph)
    end_time = time.time()
    print(f"Directed graph is 2-vertex strongly biconnected: {is_2_vsb} (checked in {end_time - start_time:.6f} seconds).")

if __name__ == "__main__":
    main()
