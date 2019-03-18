#!/usr/bin/env python3
''' module contains functions for converting directed graphs to undirected graph '''

def symmetric_completion(directed_graph):
    ''' calculate adjacency list representation of the underlying graph for a directed graph '''
    undirected_graph = {}
    for vertex, neighbors in directed_graph.items():
        undirected_graph[vertex] = set(neighbors)

    for vertex, neighbors in directed_graph.items():
        for neighbor in neighbors:
            if neighbor in undirected_graph:
                undirected_graph[neighbor].add(vertex)
            else:
                undirected_graph[neighbor] = set(vertex)

    return undirected_graph
