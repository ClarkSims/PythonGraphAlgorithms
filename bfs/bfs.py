#!/usr/bin/env python3
import pdb

def simple_breadth_first_search( directed_graph, vertex0, vertex1):
    if vertex0 == vertex1:
        return 0
    visited = {vertex0}
    boundary = {vertex0}
    distance = 0
    while boundary:
        next_boundary = set()
        distance += 1
        for vertex in boundary:
            for neighbor in directed_graph[vertex]:
                if neighbor not in visited:
                    if neighbor == vertex1:
                        return distance
                    visited.add(neighbor)
                    next_boundary.add(neighbor)
        boundary = next_boundary
    raise IndexError( "{} is not connected to {}".format(vertex1,vertex0))


def double_sided_breadth_first_search(directed_graph, vertex0, vertex1):
    boundary0 = {vertex0}
    boundary1 = {vertex1}

    #mark verticies
    visited = {vertex0 : vertex0, vertex1 : vertex1}
 
    distance = 0
    common_vertex = None
    while (boundary0 or boundary1) and common_vertex is None:
        if boundary0 and boundary1:
            if len(boundary0) <= len(boundary1):
                common_vertex, boundary0, path_increment = expand_left_boundary(
                    boundary0, boundary1, visited, directed_graph, vertex0)
            else:
                common_vertex, boundary1, path_increment = expand_left_boundary(
                    boundary1, boundary0, visited, directed_graph, vertex1)
        elif boundary0:
            common_vertex, boundary0, path_increment = expand_left_boundary(
                boundary0, boundary1, visited, directed_graph, vertex0)
        elif boundary1:
            common_vertex, boundary1, path_increment = expand_left_boundary(
                boundary1, boundary0, visited, directed_graph, vertex1)
        distance+=path_increment
        
    if common_vertex:
        return distance
    raise ValueError( "{} is not connected to {}".format(vertex1,vertex0))


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

