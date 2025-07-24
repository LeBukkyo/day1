"""
Graph Search Algorithms: Breadth-First Search (BFS) and Depth-First Search (DFS)

This module implements both BFS and DFS algorithms for graph traversal,
including path finding and connected component detection.
"""

from collections import deque, defaultdict
from typing import List, Dict, Set, Optional, Tuple


class Graph:
    """
    A graph data structure that supports both directed and undirected graphs.
    Supports BFS and DFS traversal algorithms.
    """
    
    def __init__(self, directed: bool = False):
        """
        Initialize a graph.
        
        Args:
            directed (bool): Whether the graph is directed or undirected
        """
        self.adjacency_list: Dict[str, List[str]] = defaultdict(list)
        self.directed = directed
    
    def add_edge(self, start: str, end: str) -> None:
        """
        Add an edge to the graph.
        
        Args:
            start (str): Starting vertex
            end (str): Ending vertex
        """
        # Ensure both vertices exist in the adjacency list
        if start not in self.adjacency_list:
            self.adjacency_list[start] = []
        if end not in self.adjacency_list:
            self.adjacency_list[end] = []
            
        self.adjacency_list[start].append(end)
        if not self.directed:
            self.adjacency_list[end].append(start)
    
    def add_vertex(self, vertex: str) -> None:
        """
        Add a vertex to the graph.
        
        Args:
            vertex (str): Vertex to add
        """
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
    
    def get_vertices(self) -> List[str]:
        """Get all vertices in the graph."""
        return list(self.adjacency_list.keys())
    
    def get_neighbors(self, vertex: str) -> List[str]:
        """Get neighbors of a vertex."""
        return self.adjacency_list.get(vertex, [])
    
    def breadth_first_search(self, start: str) -> List[str]:
        """
        Perform Breadth-First Search starting from a given vertex.
        
        Args:
            start (str): Starting vertex for BFS
            
        Returns:
            List[str]: List of vertices in BFS order
        """
        if start not in self.adjacency_list:
            return []
        
        visited: Set[str] = set()
        queue: deque = deque([start])
        result: List[str] = []
        
        while queue:
            current = queue.popleft()
            
            if current not in visited:
                visited.add(current)
                result.append(current)
                
                # Add unvisited neighbors to queue
                for neighbor in self.adjacency_list[current]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        
        return result
    
    def depth_first_search(self, start: str) -> List[str]:
        """
        Perform Depth-First Search starting from a given vertex (iterative).
        
        Args:
            start (str): Starting vertex for DFS
            
        Returns:
            List[str]: List of vertices in DFS order
        """
        if start not in self.adjacency_list:
            return []
        
        visited: Set[str] = set()
        stack: List[str] = [start]
        result: List[str] = []
        
        while stack:
            current = stack.pop()
            
            if current not in visited:
                visited.add(current)
                result.append(current)
                
                # Add unvisited neighbors to stack (in reverse order for consistent ordering)
                for neighbor in reversed(self.adjacency_list[current]):
                    if neighbor not in visited:
                        stack.append(neighbor)
        
        return result
    
    def dfs_recursive(self, start: str, visited: Optional[Set[str]] = None) -> List[str]:
        """
        Perform Depth-First Search recursively.
        
        Args:
            start (str): Starting vertex for DFS
            visited (Set[str], optional): Set of visited vertices
            
        Returns:
            List[str]: List of vertices in DFS order
        """
        if visited is None:
            visited = set()
        
        if start not in self.adjacency_list or start in visited:
            return []
        
        visited.add(start)
        result = [start]
        
        for neighbor in self.adjacency_list[start]:
            if neighbor not in visited:
                result.extend(self.dfs_recursive(neighbor, visited))
        
        return result
    
    def find_path_bfs(self, start: str, target: str) -> Optional[List[str]]:
        """
        Find shortest path between two vertices using BFS.
        
        Args:
            start (str): Starting vertex
            target (str): Target vertex
            
        Returns:
            Optional[List[str]]: Shortest path from start to target, or None if no path exists
        """
        if start not in self.adjacency_list or target not in self.adjacency_list:
            return None
        
        if start == target:
            return [start]
        
        visited: Set[str] = set()
        queue: deque = deque([(start, [start])])
        
        while queue:
            current, path = queue.popleft()
            
            if current in visited:
                continue
                
            visited.add(current)
            
            for neighbor in self.adjacency_list[current]:
                if neighbor == target:
                    return path + [neighbor]
                
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
        
        return None
    
    def find_path_dfs(self, start: str, target: str) -> Optional[List[str]]:
        """
        Find a path between two vertices using DFS.
        
        Args:
            start (str): Starting vertex
            target (str): Target vertex
            
        Returns:
            Optional[List[str]]: A path from start to target, or None if no path exists
        """
        if start not in self.adjacency_list or target not in self.adjacency_list:
            return None
        
        if start == target:
            return [start]
        
        visited: Set[str] = set()
        stack: List[Tuple[str, List[str]]] = [(start, [start])]
        
        while stack:
            current, path = stack.pop()
            
            if current in visited:
                continue
                
            visited.add(current)
            
            for neighbor in self.adjacency_list[current]:
                if neighbor == target:
                    return path + [neighbor]
                
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
        
        return None
    
    def connected_components_bfs(self) -> List[List[str]]:
        """
        Find all connected components using BFS.
        
        Returns:
            List[List[str]]: List of connected components, each as a list of vertices
        """
        visited: Set[str] = set()
        components: List[List[str]] = []
        
        for vertex in self.adjacency_list:
            if vertex not in visited:
                component = []
                queue: deque = deque([vertex])
                
                while queue:
                    current = queue.popleft()
                    if current not in visited:
                        visited.add(current)
                        component.append(current)
                        
                        for neighbor in self.adjacency_list[current]:
                            if neighbor not in visited:
                                queue.append(neighbor)
                
                if component:
                    components.append(component)
        
        return components
    
    def is_connected(self) -> bool:
        """
        Check if the graph is connected (for undirected graphs).
        
        Returns:
            bool: True if the graph is connected, False otherwise
        """
        if not self.adjacency_list:
            return True
        
        # Start BFS from the first vertex
        start = next(iter(self.adjacency_list))
        visited = set(self.breadth_first_search(start))
        
        # Check if all vertices were visited
        return len(visited) == len(self.adjacency_list)
    
    def __str__(self) -> str:
        """String representation of the graph."""
        graph_type = "Directed" if self.directed else "Undirected"
        result = f"{graph_type} Graph:\n"
        
        for vertex, neighbors in self.adjacency_list.items():
            result += f"  {vertex}: {neighbors}\n"
        
        return result
