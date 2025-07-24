# Graph Search Algorithms: BFS and DFS

A comprehensive Python implementation of **Breadth-First Search (BFS)** and **Depth-First Search (DFS)** algorithms with practical examples and thorough testing.

## 🚀 Features

- **Complete Graph Implementation**: Support for both directed and undirected graphs
- **Multiple Search Algorithms**:
  - Breadth-First Search (BFS) - iterative
  - Depth-First Search (DFS) - both iterative and recursive implementations
- **Advanced Functionality**:
  - Shortest path finding (BFS guarantees optimal solution)
  - Connected components detection
  - Graph connectivity checking
- **Comprehensive Examples**: Real-world applications including maze solving
- **Extensive Testing**: 25+ unit tests ensuring correctness
- **Clean, Documented Code**: Type hints and detailed docstrings

## 📋 Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Algorithms Overview](#algorithms-overview)
- [Usage Examples](#usage-examples)
- [API Reference](#api-reference)
- [Running Tests](#running-tests)
- [Performance](#performance)
- [Contributing](#contributing)
- [License](#license)

## 🛠 Installation

Clone this repository:

```bash
git clone https://github.com/your-username/graph-search-algorithms.git
cd graph-search-algorithms
```

No external dependencies required! This project uses only Python standard library.

**Requirements:**
- Python 3.7 or higher
- Standard library modules: `collections`, `typing`

## ⚡ Quick Start

```python
from graph_search_algorithms import Graph

# Create an undirected graph
graph = Graph(directed=False)

# Add edges
graph.add_edge('A', 'B')
graph.add_edge('B', 'C')
graph.add_edge('A', 'C')

# Perform BFS
bfs_result = graph.breadth_first_search('A')
print(f"BFS traversal: {bfs_result}")
# Output: BFS traversal: ['A', 'B', 'C']

# Perform DFS
dfs_result = graph.depth_first_search('A')
print(f"DFS traversal: {dfs_result}")
# Output: DFS traversal: ['A', 'B', 'C']

# Find shortest path
path = graph.find_path_bfs('A', 'C')
print(f"Shortest path from A to C: {path}")
# Output: Shortest path from A to C: ['A', 'C']
```

## 🔍 Algorithms Overview

### Breadth-First Search (BFS)
- **Strategy**: Explores all vertices at the current depth before moving to vertices at the next depth
- **Data Structure**: Queue (FIFO)
- **Guarantee**: Finds the shortest path in unweighted graphs
- **Time Complexity**: O(V + E)
- **Space Complexity**: O(V)
- **Best For**: Shortest path problems, level-order traversal

### Depth-First Search (DFS)
- **Strategy**: Explores as far as possible along each branch before backtracking
- **Data Structure**: Stack (LIFO) or recursion
- **Guarantee**: Visits all reachable vertices
- **Time Complexity**: O(V + E)
- **Space Complexity**: O(V)
- **Best For**: Detecting cycles, topological sorting, finding connected components

## 💡 Usage Examples

### Basic Graph Operations

```python
from graph_search_algorithms import Graph

# Create a directed graph
graph = Graph(directed=True)

# Add vertices and edges
graph.add_vertex('Start')
graph.add_edge('Start', 'A')
graph.add_edge('A', 'B')
graph.add_edge('B', 'End')

# Traverse the graph
print("BFS:", graph.breadth_first_search('Start'))
print("DFS:", graph.depth_first_search('Start'))
```

### Pathfinding

```python
# Find paths between vertices
bfs_path = graph.find_path_bfs('Start', 'End')  # Shortest path
dfs_path = graph.find_path_dfs('Start', 'End')  # Any valid path

print(f"BFS path (shortest): {bfs_path}")
print(f"DFS path: {dfs_path}")
```

### Maze Solving

```python
# Create a grid-like maze
maze = Graph(directed=False)
maze.add_edge('0,0', '0,1')  # Grid positions
maze.add_edge('0,1', '0,2')
maze.add_edge('0,0', '1,0')
# ... more connections

# Solve the maze
solution = maze.find_path_bfs('0,0', '2,2')
print(f"Maze solution: {solution}")
```

### Connected Components

```python
# Find all connected components
components = graph.connected_components_bfs()
print(f"Connected components: {components}")

# Check if graph is connected
is_connected = graph.is_connected()
print(f"Graph is connected: {is_connected}")
```

## 📚 API Reference

### Graph Class

#### Constructor
```python
Graph(directed: bool = False)
```

#### Methods

| Method | Description | Time Complexity |
|--------|-------------|-----------------|
| `add_vertex(vertex)` | Add a single vertex | O(1) |
| `add_edge(start, end)` | Add an edge between vertices | O(1) |
| `breadth_first_search(start)` | BFS traversal from start vertex | O(V + E) |
| `depth_first_search(start)` | DFS traversal (iterative) | O(V + E) |
| `dfs_recursive(start)` | DFS traversal (recursive) | O(V + E) |
| `find_path_bfs(start, target)` | Find shortest path using BFS | O(V + E) |
| `find_path_dfs(start, target)` | Find any path using DFS | O(V + E) |
| `connected_components_bfs()` | Find all connected components | O(V + E) |
| `is_connected()` | Check if graph is connected | O(V + E) |
| `get_vertices()` | Get all vertices | O(V) |
| `get_neighbors(vertex)` | Get neighbors of a vertex | O(1) |

## 🧪 Running Tests

Run the comprehensive test suite:

```bash
python3 test_graph_algorithms.py
```

The test suite includes:
- Graph construction and manipulation
- BFS and DFS correctness
- Pathfinding functionality
- Connected components detection
- Edge cases and error handling

Expected output:
```
Running Graph Search Algorithm Tests...
==================================================
...
----------------------------------------------------------------------
Ran 25 tests in 0.001s

OK
==================================================
All tests PASSED! ✅
```

## 🎯 Examples and Demonstrations

Run the comprehensive demonstration:

```bash
python3 examples.py
```

This will showcase:
1. **Basic Traversal**: BFS vs DFS comparison
2. **Pathfinding**: Shortest path vs any path
3. **Directed Graphs**: Behavior with directed edges
4. **Connected Components**: Finding disconnected parts
5. **Performance Comparison**: Memory and path optimality
6. **Maze Solving**: Practical application example

## ⚡ Performance

### Time Complexity
- **Graph Traversal**: O(V + E) for both BFS and DFS
- **Pathfinding**: O(V + E) in worst case
- **Connected Components**: O(V + E)

### Space Complexity
- **BFS**: O(V) for queue storage
- **DFS (iterative)**: O(V) for stack storage
- **DFS (recursive)**: O(V) for recursion stack

### When to Use Each Algorithm

| Use Case | Recommended Algorithm | Reason |
|----------|----------------------|---------|
| Shortest path in unweighted graph | BFS | Guarantees optimal solution |
| Memory-constrained environment | DFS | Lower memory usage |
| Finding any path quickly | DFS | May find solution faster |
| Web crawling (by levels) | BFS | Systematic level exploration |
| Detecting cycles | DFS | Natural backtracking |
| Topological sorting | DFS | Post-order traversal |

## 🗂 Project Structure

```
graph-search-algorithms/
├── graph_search_algorithms.py  # Main implementation
├── examples.py                 # Comprehensive examples
├── test_graph_algorithms.py    # Unit tests
├── README.md                   # This file
└── requirements.txt            # Dependencies (none!)
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes** and add tests
4. **Run the test suite**: `python3 test_graph_algorithms.py`
5. **Commit your changes**: `git commit -m 'Add amazing feature'`
6. **Push to the branch**: `git push origin feature/amazing-feature`
7. **Open a Pull Request**

### Guidelines
- Follow PEP 8 style guidelines
- Add docstrings for new methods
- Include unit tests for new functionality
- Update README if needed

## 📖 Educational Resources

### Learn More About Graph Algorithms
- [Graph Theory Basics](https://en.wikipedia.org/wiki/Graph_theory)
- [BFS Algorithm](https://en.wikipedia.org/wiki/Breadth-first_search)
- [DFS Algorithm](https://en.wikipedia.org/wiki/Depth-first_search)

### Applications
- **Social Networks**: Friend recommendations, shortest path between users
- **GPS Navigation**: Route finding algorithms
- **Web Crawling**: Systematic website exploration
- **Game AI**: Pathfinding for NPCs
- **Network Analysis**: Finding connected components in networks

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

Created with ❤️ by Collin

---

## 🌟 Star this Repository

If you found this implementation helpful, please give it a star! ⭐

It helps others discover this resource and motivates continued improvement.

---

*Happy coding and graph traversing!* 🚀 
