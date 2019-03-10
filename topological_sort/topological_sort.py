#!/usr/bin/env python3
'''
    This module implements a topological sort.
    https://en.wikipedia.org/wiki/Topological_sorting
    It also detects circular dependences and throws an invalid index error,
    if one is found. It saves the root dependencies so that the system can be
    easily built in parallel.
'''
VERBOSE = False

def topological_sort(dag, root_nodes):
    ''' dag: represents a directed acyclic graph
           : has the following interface:
               __getitem__ which maps vertex to iterable container of vertecies
               must implement __iter__ and __contains__
        vertex: must be support __hash__ and __eq__
        root_nodes: represents an iterable container which supports clear and add
    '''
    root_nodes.clear()
    visited = {vertex : False for vertex in dag}
    traversed = []

    for vertex in dag:
        if not visited[vertex]:
            topology_helper(vertex, dag, visited, traversed, root_nodes)

    return list(reversed(traversed))


def topology_helper(\
    vertex,\
    dag,\
    visited,\
    traversed,\
    root_nodes,\
    call_stack_set=None,\
    call_stack_list=None):
    '''
        This function does a depth first search starting at vertex.
        call_stack_set is a set which is updated at each iteration to represent the
        the path of the current vertex, from the start vertex.
        call_stack_list is the list which is the path.
        If vertex has no children, then it is a root node, in the inverted
        dependency tree, and added to root_nodes.
    '''
    if VERBOSE:
        print("****************")
        print("entering topology_helper with vertex")
        print("vertex = ", vertex)
        print("call stack list = ", call_stack_list)
        print("traversed = ", traversed)
    if not call_stack_set:
        call_stack_set = set()
        call_stack_list = []
        traversed.append(vertex)
#        pdb.set_trace()
    else:
        if vertex in call_stack_set:
            pretty_error = "circular dependence {}".format(vertex)
            vindex = call_stack_list.index(vertex)
            for vert in call_stack_list[vindex+1:]:
                pretty_error += "=> {}".format(vert)
            pretty_error += "=> {}".format(vertex)
            print("call stack list = ", call_stack_list)
            raise IndexError(pretty_error)
    call_stack_list.append(vertex)
    call_stack_set.add(vertex)
    visited[vertex] = True
    if dag[vertex]:
        for neighbor in dag[vertex]:
            if not visited[neighbor]:
                traversed.append(neighbor)

    if dag[vertex]:
        for neighbor in dag[vertex]:
            if not visited[neighbor]:
                if VERBOSE:
                    print("****************")
                    print("calling topology_helper for vertex neighbor")
                    print("vertex = ", vertex)
                    print("neighbor = ", neighbor)
                    print("call stack list = ", call_stack_list)
                topology_helper(
                    neighbor,
                    dag,
                    visited,
                    traversed,
                    root_nodes,
                    call_stack_set,
                    call_stack_list)
    else:
        root_nodes.append(vertex)

    if VERBOSE:
        print("****************")
        print("leaving topology_helper with vertex")
        print("vertex = ", vertex)
        print("call stack list = ", call_stack_list)
        print("traversed = ", traversed)
