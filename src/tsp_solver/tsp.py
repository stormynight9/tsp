"""
Implementation of the Traveling Salesman Problem (TSP) using a naive approach.

This module provides a solution to the TSP using a brute-force approach that
examines all possible permutations of cities to find the minimum cost path.

Note:
    This implementation is suitable for small instances of TSP (typically n ≤ 10)
    due to its factorial time complexity.
"""

from sys import maxsize 
from itertools import permutations

# Number of vertices in the graph
V = 4

def travellingSalesmanProblem(graph, s): 
    """
    Find the minimum weight Hamiltonian cycle in a graph starting from a specified vertex.
    
    This function implements a naive solution to the Traveling Salesman Problem
    by generating all possible permutations of vertices and finding the minimum
    cost path that visits all vertices exactly once and returns to the start.
    
    Args:
        graph (List[List[int]]): A V x V matrix representing the weighted graph.
            graph[i][j] represents the weight of edge from vertex i to vertex j.
        s (int): The starting vertex (0 <= s < V)
    
    Returns:
        int: The minimum weight of the Hamiltonian cycle starting from vertex s.
            If no valid path exists, returns sys.maxsize
    
    Raises:
        ValueError: If the graph dimensions don't match V x V or if s is not in range [0, V-1]
        
    Example:
        >>> graph = [
        ...     [0, 10, 15, 20],
        ...     [10, 0, 35, 25],
        ...     [15, 35, 0, 30],
        ...     [20, 25, 30, 0]
        ... ]
        >>> travellingSalesmanProblem(graph, 0)
        80
    """
    # Input validation
    if len(graph) != V or any(len(row) != V for row in graph):
        raise ValueError(f"Graph must be a {V}x{V} matrix")
    if not 0 <= s < V:
        raise ValueError(f"Starting vertex must be between 0 and {V-1}")
    
    # Store all vertices apart from source vertex 
    vertex = [i for i in range(V) if i != s]
    
    # Store minimum weight Hamiltonian Cycle 
    min_path = maxsize 
    
    # Generate all possible permutations of vertices
    next_permutation = permutations(vertex)
    
    # Try each permutation to find minimum cost
    for i in next_permutation:
        # Store current path weight(cost) 
        current_pathweight = 0
        
        # Compute current path weight 
        k = s 
        for j in i: 
            current_pathweight += graph[k][j] 
            k = j 
        current_pathweight += graph[k][s] 
        
        # Update minimum 
        min_path = min(min_path, current_pathweight) 
        
    return min_path 

