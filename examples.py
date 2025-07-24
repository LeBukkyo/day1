"""
Example usage of Graph Search Algorithms (BFS and DFS)

This script demonstrates various applications of BFS and DFS algorithms
including graph traversal, pathfinding, and connected components.
"""

from graph_search_algorithms import Graph


def create_sample_undirected_graph() -> Graph:
    """Create a sample undirected graph for demonstration."""
    graph = Graph(directed=False)
    
    # Add vertices
    vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    for vertex in vertices:
        graph.add_vertex(vertex)
    
    # Add edges to create a connected graph
    edges = [
        ('A', 'B'), ('A', 'C'),
        ('B', 'D'), ('B', 'E'),
        ('C', 'F'),
        ('D', 'G'),
        ('E', 'G')
    ]
    
    for start, end in edges:
        graph.add_edge(start, end)
    
    return graph


def create_sample_directed_graph() -> Graph:
    """Create a sample directed graph for demonstration."""
    graph = Graph(directed=True)
    
    # Add vertices
    vertices = ['1', '2', '3', '4', '5', '6']
    for vertex in vertices:
        graph.add_vertex(vertex)
    
    # Add directed edges
    edges = [
        ('1', '2'), ('1', '3'),
        ('2', '4'), ('2', '5'),
        ('3', '6'),
        ('4', '6'),
        ('5', '6')
    ]
    
    for start, end in edges:
        graph.add_edge(start, end)
    
    return graph


def create_disconnected_graph() -> Graph:
    """Create a graph with multiple disconnected components."""
    graph = Graph(directed=False)
    
    # Component 1
    graph.add_edge('A', 'B')
    graph.add_edge('B', 'C')
    
    # Component 2
    graph.add_edge('D', 'E')
    
    # Component 3 (single vertex)
    graph.add_vertex('F')
    
    return graph


def demonstrate_basic_traversal():
    """Demonstrate basic BFS and DFS traversal."""
    print("=" * 60)
    print("BASIC GRAPH TRAVERSAL DEMONSTRATION")
    print("=" * 60)
    
    graph = create_sample_undirected_graph()
    print("Sample Undirected Graph:")
    print(graph)
    
    # BFS traversal
    start_vertex = 'A'
    bfs_result = graph.breadth_first_search(start_vertex)
    print(f"BFS traversal starting from '{start_vertex}': {bfs_result}")
    
    # DFS traversal (iterative)
    dfs_result = graph.depth_first_search(start_vertex)
    print(f"DFS traversal (iterative) starting from '{start_vertex}': {dfs_result}")
    
    # DFS traversal (recursive)
    dfs_recursive_result = graph.dfs_recursive(start_vertex)
    print(f"DFS traversal (recursive) starting from '{start_vertex}': {dfs_recursive_result}")
    
    print()


def demonstrate_pathfinding():
    """Demonstrate pathfinding using BFS and DFS."""
    print("=" * 60)
    print("PATHFINDING DEMONSTRATION")
    print("=" * 60)
    
    graph = create_sample_undirected_graph()
    print("Sample Undirected Graph:")
    print(graph)
    
    # Find paths between different vertex pairs
    test_pairs = [('A', 'G'), ('B', 'F'), ('A', 'E'), ('C', 'D')]
    
    for start, end in test_pairs:
        bfs_path = graph.find_path_bfs(start, end)
        dfs_path = graph.find_path_dfs(start, end)
        
        print(f"Path from '{start}' to '{end}':")
        print(f"  BFS (shortest): {bfs_path}")
        print(f"  DFS: {dfs_path}")
        
        if bfs_path and dfs_path:
            print(f"  BFS path length: {len(bfs_path)}")
            print(f"  DFS path length: {len(dfs_path)}")
        print()


def demonstrate_directed_graph():
    """Demonstrate algorithms on directed graphs."""
    print("=" * 60)
    print("DIRECTED GRAPH DEMONSTRATION")
    print("=" * 60)
    
    graph = create_sample_directed_graph()
    print("Sample Directed Graph:")
    print(graph)
    
    start_vertex = '1'
    
    # Traversal on directed graph
    bfs_result = graph.breadth_first_search(start_vertex)
    dfs_result = graph.depth_first_search(start_vertex)
    
    print(f"BFS traversal starting from '{start_vertex}': {bfs_result}")
    print(f"DFS traversal starting from '{start_vertex}': {dfs_result}")
    
    # Pathfinding on directed graph
    path_bfs = graph.find_path_bfs('1', '6')
    path_dfs = graph.find_path_dfs('1', '6')
    
    print(f"Path from '1' to '6':")
    print(f"  BFS: {path_bfs}")
    print(f"  DFS: {path_dfs}")
    print()


def demonstrate_connected_components():
    """Demonstrate finding connected components."""
    print("=" * 60)
    print("CONNECTED COMPONENTS DEMONSTRATION")
    print("=" * 60)
    
    graph = create_disconnected_graph()
    print("Disconnected Graph:")
    print(graph)
    
    components = graph.connected_components_bfs()
    print(f"Connected components: {components}")
    print(f"Number of components: {len(components)}")
    print(f"Is graph connected? {graph.is_connected()}")
    print()
    
    # Compare with connected graph
    connected_graph = create_sample_undirected_graph()
    print("Connected Graph:")
    connected_components = connected_graph.connected_components_bfs()
    print(f"Connected components: {connected_components}")
    print(f"Number of components: {len(connected_components)}")
    print(f"Is graph connected? {connected_graph.is_connected()}")
    print()


def demonstrate_performance_comparison():
    """Demonstrate performance characteristics of BFS vs DFS."""
    print("=" * 60)
    print("PERFORMANCE CHARACTERISTICS")
    print("=" * 60)
    
    # Create a larger graph
    graph = Graph(directed=False)
    
    # Create a linear chain
    for i in range(10):
        graph.add_vertex(str(i))
        if i > 0:
            graph.add_edge(str(i-1), str(i))
    
    print("Linear Chain Graph (0 -> 1 -> 2 -> ... -> 9):")
    print(graph)
    
    # Find path from start to end
    bfs_path = graph.find_path_bfs('0', '9')
    dfs_path = graph.find_path_dfs('0', '9')
    
    print(f"Path from '0' to '9':")
    print(f"  BFS (guaranteed shortest): {bfs_path}")
    print(f"  DFS (may not be shortest): {dfs_path}")
    print()
    
    print("Key Differences:")
    print("- BFS finds the shortest path (minimum number of edges)")
    print("- DFS finds any path, which may not be optimal")
    print("- BFS uses more memory (queue) but guarantees shortest path")
    print("- DFS uses less memory (stack) but path may be longer")
    print()


def create_maze_like_graph() -> Graph:
    """Create a maze-like graph to demonstrate practical usage."""
    graph = Graph(directed=False)
    
    # Create a grid-like structure (simplified maze)
    # Positions: (row, col)
    positions = [
        (0,0), (0,1), (0,2),
        (1,0), (1,2),
        (2,0), (2,1), (2,2)
    ]
    
    # Add vertices
    for pos in positions:
        graph.add_vertex(f"{pos[0]},{pos[1]}")
    
    # Add edges (connections between adjacent cells)
    connections = [
        ((0,0), (0,1)), ((0,1), (0,2)),  # Top row
        ((0,0), (1,0)),                   # Left column
        ((0,2), (1,2)),                   # Right column  
        ((1,0), (2,0)), ((1,2), (2,2)),   # Down connections
        ((2,0), (2,1)), ((2,1), (2,2))   # Bottom row
    ]
    
    for (r1,c1), (r2,c2) in connections:
        graph.add_edge(f"{r1},{c1}", f"{r2},{c2}")
    
    return graph


def demonstrate_maze_solving():
    """Demonstrate maze solving using BFS and DFS."""
    print("=" * 60)
    print("MAZE SOLVING DEMONSTRATION")
    print("=" * 60)
    
    maze = create_maze_like_graph()
    print("Maze-like Graph (Grid positions):")
    print(maze)
    
    start = "0,0"  # Top-left
    end = "2,2"    # Bottom-right
    
    bfs_path = maze.find_path_bfs(start, end)
    dfs_path = maze.find_path_dfs(start, end)
    
    print(f"Solving maze from {start} to {end}:")
    print(f"  BFS path (shortest): {bfs_path}")
    print(f"  DFS path: {dfs_path}")
    
    if bfs_path and dfs_path:
        print(f"  BFS steps: {len(bfs_path) - 1}")
        print(f"  DFS steps: {len(dfs_path) - 1}")
    print()


def main():
    """Run all demonstrations."""
    print("GRAPH SEARCH ALGORITHMS DEMONSTRATION")
    print("=====================================")
    print("This script demonstrates Breadth-First Search (BFS) and Depth-First Search (DFS)")
    print("algorithms implemented in Python.\n")
    
    demonstrate_basic_traversal()
    demonstrate_pathfinding()
    demonstrate_directed_graph()
    demonstrate_connected_components()
    demonstrate_performance_comparison()
    demonstrate_maze_solving()
    
    print("=" * 60)
    print("DEMONSTRATION COMPLETE")
    print("=" * 60)
    print("Key Takeaways:")
    print("1. BFS explores nodes level by level (breadth-first)")
    print("2. DFS explores as far as possible before backtracking (depth-first)")
    print("3. BFS guarantees shortest path in unweighted graphs")
    print("4. DFS uses less memory but may find longer paths")
    print("5. Both have O(V + E) time complexity for traversal")
    print("6. Choice depends on specific use case and requirements")


if __name__ == "__main__":
    main() 