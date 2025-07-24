"""
Unit tests for Graph Search Algorithms (BFS and DFS)

This module contains comprehensive tests for the graph data structure
and its BFS and DFS implementation.
"""

import unittest
from graph_search_algorithms import Graph


class TestGraph(unittest.TestCase):
    """Test cases for the Graph class and its methods."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.undirected_graph = Graph(directed=False)
        self.directed_graph = Graph(directed=True)
        
        # Create a simple undirected graph
        # A --- B --- D
        # |     |     |
        # C --- E --- F
        edges_undirected = [
            ('A', 'B'), ('A', 'C'), ('B', 'D'), 
            ('B', 'E'), ('C', 'E'), ('D', 'F'), ('E', 'F')
        ]
        for start, end in edges_undirected:
            self.undirected_graph.add_edge(start, end)
        
        # Create a simple directed graph
        # 1 -> 2 -> 4
        # |    |    |
        # v    v    v
        # 3 -> 5 -> 6
        edges_directed = [
            ('1', '2'), ('1', '3'), ('2', '4'), 
            ('2', '5'), ('3', '5'), ('4', '6'), ('5', '6')
        ]
        for start, end in edges_directed:
            self.directed_graph.add_edge(start, end)
    
    def test_graph_initialization(self):
        """Test graph initialization."""
        undirected = Graph(directed=False)
        directed = Graph(directed=True)
        
        self.assertFalse(undirected.directed)
        self.assertTrue(directed.directed)
        self.assertEqual(len(undirected.adjacency_list), 0)
        self.assertEqual(len(directed.adjacency_list), 0)
    
    def test_add_vertex(self):
        """Test adding vertices to the graph."""
        graph = Graph()
        graph.add_vertex('A')
        
        self.assertIn('A', graph.adjacency_list)
        self.assertEqual(graph.adjacency_list['A'], [])
    
    def test_add_edge_undirected(self):
        """Test adding edges to undirected graph."""
        graph = Graph(directed=False)
        graph.add_edge('A', 'B')
        
        self.assertIn('B', graph.adjacency_list['A'])
        self.assertIn('A', graph.adjacency_list['B'])
    
    def test_add_edge_directed(self):
        """Test adding edges to directed graph."""
        graph = Graph(directed=True)
        graph.add_edge('A', 'B')
        
        self.assertIn('B', graph.adjacency_list['A'])
        self.assertNotIn('A', graph.adjacency_list['B'])
    
    def test_get_vertices(self):
        """Test getting all vertices."""
        vertices = self.undirected_graph.get_vertices()
        expected_vertices = ['A', 'B', 'C', 'D', 'E', 'F']
        
        self.assertEqual(set(vertices), set(expected_vertices))
    
    def test_get_neighbors(self):
        """Test getting neighbors of a vertex."""
        neighbors_a = self.undirected_graph.get_neighbors('A')
        neighbors_nonexistent = self.undirected_graph.get_neighbors('Z')
        
        self.assertEqual(set(neighbors_a), {'B', 'C'})
        self.assertEqual(neighbors_nonexistent, [])


class TestBFS(unittest.TestCase):
    """Test cases for Breadth-First Search algorithm."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.graph = Graph(directed=False)
        
        # Create a simple graph for testing
        # A --- B --- D
        # |           |
        # C --------- E
        edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'E'), ('D', 'E')]
        for start, end in edges:
            self.graph.add_edge(start, end)
    
    def test_bfs_traversal(self):
        """Test BFS traversal order."""
        result = self.graph.breadth_first_search('A')
        
        # BFS should visit A first, then its neighbors B and C, then D and E
        self.assertEqual(result[0], 'A')
        self.assertIn('B', result[1:3])  # B and C should be visited next
        self.assertIn('C', result[1:3])
        self.assertIn('D', result[3:])   # D and E should be visited last
        self.assertIn('E', result[3:])
        self.assertEqual(len(result), 5)
    
    def test_bfs_nonexistent_vertex(self):
        """Test BFS with non-existent starting vertex."""
        result = self.graph.breadth_first_search('Z')
        self.assertEqual(result, [])
    
    def test_bfs_single_vertex(self):
        """Test BFS on a graph with single vertex."""
        single_graph = Graph()
        single_graph.add_vertex('A')
        
        result = single_graph.breadth_first_search('A')
        self.assertEqual(result, ['A'])
    
    def test_bfs_disconnected_graph(self):
        """Test BFS on disconnected graph."""
        disconnected = Graph()
        disconnected.add_edge('A', 'B')
        disconnected.add_edge('C', 'D')
        
        result = disconnected.breadth_first_search('A')
        self.assertEqual(set(result), {'A', 'B'})  # Should only visit connected component


class TestDFS(unittest.TestCase):
    """Test cases for Depth-First Search algorithm."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.graph = Graph(directed=False)
        
        # Create a simple graph for testing
        # A --- B --- D
        # |           |
        # C --------- E
        edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'E'), ('D', 'E')]
        for start, end in edges:
            self.graph.add_edge(start, end)
    
    def test_dfs_traversal(self):
        """Test DFS traversal."""
        result = self.graph.depth_first_search('A')
        
        # DFS should visit A first
        self.assertEqual(result[0], 'A')
        self.assertEqual(len(result), 5)
        
        # All vertices should be visited
        self.assertEqual(set(result), {'A', 'B', 'C', 'D', 'E'})
    
    def test_dfs_recursive(self):
        """Test recursive DFS implementation."""
        result = self.graph.dfs_recursive('A')
        
        # DFS should visit A first
        self.assertEqual(result[0], 'A')
        self.assertEqual(len(result), 5)
        
        # All vertices should be visited
        self.assertEqual(set(result), {'A', 'B', 'C', 'D', 'E'})
    
    def test_dfs_nonexistent_vertex(self):
        """Test DFS with non-existent starting vertex."""
        result = self.graph.depth_first_search('Z')
        self.assertEqual(result, [])
        
        result_recursive = self.graph.dfs_recursive('Z')
        self.assertEqual(result_recursive, [])
    
    def test_dfs_single_vertex(self):
        """Test DFS on a graph with single vertex."""
        single_graph = Graph()
        single_graph.add_vertex('A')
        
        result = single_graph.depth_first_search('A')
        self.assertEqual(result, ['A'])
        
        result_recursive = single_graph.dfs_recursive('A')
        self.assertEqual(result_recursive, ['A'])


class TestPathfinding(unittest.TestCase):
    """Test cases for pathfinding algorithms."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.graph = Graph(directed=False)
        
        # Create a simple path: A - B - C - D
        edges = [('A', 'B'), ('B', 'C'), ('C', 'D')]
        for start, end in edges:
            self.graph.add_edge(start, end)
    
    def test_bfs_pathfinding(self):
        """Test BFS pathfinding."""
        path = self.graph.find_path_bfs('A', 'D')
        expected_path = ['A', 'B', 'C', 'D']
        
        self.assertEqual(path, expected_path)
    
    def test_dfs_pathfinding(self):
        """Test DFS pathfinding."""
        path = self.graph.find_path_dfs('A', 'D')
        
        # DFS should find a valid path
        self.assertIsNotNone(path)
        self.assertEqual(path[0], 'A')
        self.assertEqual(path[-1], 'D')
    
    def test_pathfinding_same_vertex(self):
        """Test pathfinding from a vertex to itself."""
        bfs_path = self.graph.find_path_bfs('A', 'A')
        dfs_path = self.graph.find_path_dfs('A', 'A')
        
        self.assertEqual(bfs_path, ['A'])
        self.assertEqual(dfs_path, ['A'])
    
    def test_pathfinding_no_path(self):
        """Test pathfinding when no path exists."""
        disconnected = Graph()
        disconnected.add_vertex('A')
        disconnected.add_vertex('B')
        
        bfs_path = disconnected.find_path_bfs('A', 'B')
        dfs_path = disconnected.find_path_dfs('A', 'B')
        
        self.assertIsNone(bfs_path)
        self.assertIsNone(dfs_path)
    
    def test_pathfinding_nonexistent_vertex(self):
        """Test pathfinding with non-existent vertices."""
        bfs_path = self.graph.find_path_bfs('A', 'Z')
        dfs_path = self.graph.find_path_dfs('Z', 'A')
        
        self.assertIsNone(bfs_path)
        self.assertIsNone(dfs_path)


class TestConnectedComponents(unittest.TestCase):
    """Test cases for connected components detection."""
    
    def test_single_component(self):
        """Test graph with single connected component."""
        graph = Graph()
        edges = [('A', 'B'), ('B', 'C'), ('C', 'A')]
        for start, end in edges:
            graph.add_edge(start, end)
        
        components = graph.connected_components_bfs()
        
        self.assertEqual(len(components), 1)
        self.assertEqual(set(components[0]), {'A', 'B', 'C'})
        self.assertTrue(graph.is_connected())
    
    def test_multiple_components(self):
        """Test graph with multiple connected components."""
        graph = Graph()
        
        # Component 1: A - B
        # Component 2: C - D - E
        # Component 3: F (isolated)
        edges = [('A', 'B'), ('C', 'D'), ('D', 'E')]
        for start, end in edges:
            graph.add_edge(start, end)
        graph.add_vertex('F')
        
        components = graph.connected_components_bfs()
        
        self.assertEqual(len(components), 3)
        self.assertFalse(graph.is_connected())
        
        # Check that all vertices are in some component
        all_vertices = set()
        for component in components:
            all_vertices.update(component)
        self.assertEqual(all_vertices, {'A', 'B', 'C', 'D', 'E', 'F'})
    
    def test_empty_graph(self):
        """Test connected components on empty graph."""
        graph = Graph()
        components = graph.connected_components_bfs()
        
        self.assertEqual(components, [])
        self.assertTrue(graph.is_connected())  # Empty graph is considered connected


class TestDirectedGraph(unittest.TestCase):
    """Test cases specific to directed graphs."""
    
    def setUp(self):
        """Set up directed graph test fixture."""
        self.graph = Graph(directed=True)
        
        # Create a simple directed graph: A -> B -> C
        edges = [('A', 'B'), ('B', 'C')]
        for start, end in edges:
            self.graph.add_edge(start, end)
    
    def test_directed_bfs(self):
        """Test BFS on directed graph."""
        result = self.graph.breadth_first_search('A')
        self.assertEqual(result, ['A', 'B', 'C'])
        
        result_from_c = self.graph.breadth_first_search('C')
        self.assertEqual(result_from_c, ['C'])  # C has no outgoing edges
    
    def test_directed_dfs(self):
        """Test DFS on directed graph."""
        result = self.graph.depth_first_search('A')
        self.assertEqual(result, ['A', 'B', 'C'])
        
        result_from_c = self.graph.depth_first_search('C')
        self.assertEqual(result_from_c, ['C'])  # C has no outgoing edges
    
    def test_directed_pathfinding(self):
        """Test pathfinding on directed graph."""
        # Forward path should exist
        path_forward = self.graph.find_path_bfs('A', 'C')
        self.assertEqual(path_forward, ['A', 'B', 'C'])
        
        # Backward path should not exist
        path_backward = self.graph.find_path_bfs('C', 'A')
        self.assertIsNone(path_backward)


def run_tests():
    """Run all tests with detailed output."""
    print("Running Graph Search Algorithm Tests...")
    print("=" * 50)
    
    # Create test suite
    test_classes = [
        TestGraph, TestBFS, TestDFS, 
        TestPathfinding, TestConnectedComponents, TestDirectedGraph
    ]
    
    suite = unittest.TestSuite()
    for test_class in test_classes:
        tests = unittest.TestLoader().loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    
    # Run tests with detailed output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Summary
    print("\n" + "=" * 50)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.wasSuccessful():
        print("All tests PASSED! ✅")
    else:
        print("Some tests FAILED! ❌")
        
    return result.wasSuccessful()


if __name__ == "__main__":
    run_tests() 