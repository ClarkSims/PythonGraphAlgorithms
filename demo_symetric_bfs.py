'''I modeled the function double_sided_breadth_first_search after the ideas in "improving Dijkstra" in Cormen et al, and the OCW course on algorithms. Note that I expand the smaller boundary, in an effort to improve effeciency. I have not seen this applied to bfs before. Does anyone know the name of this algorithm? Does it have a name? I saw the technique for doing a double sided Dijkstra algorithm, doing the iteration on the smaller vertex with smaller degree described in compsci.stackoverflow.com but can't find the page now. Does anyone know of a references for the Dijkstra style algorithm I just described?'''

#!/usr/bin/env python3

def double_sided_breadth_first_search(undirected_graph, vertex0, vertex1):
    boundary0 = {vertex0}
    boundary1 = {vertex1}

    #mark verticies
    visited = {vertex0 : vertex0, vertex1 : vertex1}
 
    distance = 0
    common_vertex = None
    while boundary0 and boundary1 and common_vertex is None:
        distance += 1
        if len(boundary0) <= len(boundary1):
            common_vertex, boundary0, path_increment = expand_left_boundary(
                boundary0, boundary1, visited, undirected_graph, vertex0)
        else:
            common_vertex, boundary1, path_increment = expand_left_boundary(
                boundary1, boundary0, visited, undirected_graph, vertex1)
    if common_vertex:
        return distance
    raise ValueError( "{} is not connected to {}".format(vertex1,vertex0))


def expand_left_boundary(lhs_boundary, rhs_boundary, visited, directed_graph, lhs_vertex):
    next_boundary = set()
    common_vertex = None
    for vertex in lhs_boundary:
        for neighbor in directed_graph[vertex]:
            if neighbor in visited:
                if visited[neighbor] != lhs_vertex:
                    common_vertex = visited[neighbor]
                    break
            else:
                next_boundary.add(neighbor)
                visited[neighbor] = lhs_vertex
    path_increment = 1 if next_boundary else 0
    return (common_vertex, next_boundary, path_increment)


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


def main():
    dg = {0 : [1], 1 : [2], 2 : [3], 3 : [4], 4 : [0]}
    ug = symmetric_completion(dg)
    print("directed graph = ", dg)
    print("undirected graph = ", ug)
    dist = double_sided_breadth_first_search(dg, 0, 2) 
    print("distance between 0 and 2 is ", dist)
 

if __name__ == '__main__':
    main()

''' output:
directed graph =  {0: [1], 1: [2], 2: [3], 3: [4], 4: [0]}
undirected graph =  {0: {1, 4}, 1: {0, 2}, 2: {1, 3}, 3: {2, 4}, 4: {0, 3}}
distance between 0 and 2 is  2
'''
