#!/usr/bin/env python3
''' library for implementing Dijkstra's algorithm '''
import math
import pdb
import inspect
from binary_min_heap_map import BinaryMinHeapMap
from undirected_graph_with_weighted_edges import UndirectedGraphWithWeightedEdges

class Dijkstra:
    ''' class that contains wrappers and data for Dijkstra '''
    def __init__(self, start_vertex=None, verticies=None, edge_weights=None):
        self._start_vertex = start_vertex
        self._verticies = verticies
        self._parents = {}
        self._bmh = BinaryMinHeapMap()
        self._distances = {}
        self._graph = UndirectedGraphWithWeightedEdges()
        if not ((start_vertex is None) or (verticies is None) or (not verticies)):
            self.init_attributes(start_vertex, verticies, edge_weights)


    def init_attributes(self, start_vertex, verticies, edge_weights):
        ''' Copy set of attributes to self '''
        if not start_vertex is None:
            svdx = verticies.index(start_vertex)
            verticies.pop(svdx)
            verticies.insert(0, start_vertex)
            raw_heap_vals = [0] + [math.inf for i in range(1, len(verticies))]
            self._bmh = BinaryMinHeapMap(verticies, raw_heap_vals)
            self._graph = \
                UndirectedGraphWithWeightedEdges(verticies,
                                                 edge_weights,
                                                 reverse_keys=True)


    def iterate(self, verbose=False):
        ''' The iteration portion of Dijkstra's algorithm '''
        if self._bmh.empty:
            raise ValueError("iterate called while self._bmh is None")
        vertex_iter = 0
        edge_iter = 0
        while not self._bmh.empty:
            if verbose:
                print("\n\n***********************************************")
                print("line = ", inspect.currentframe().f_back.f_lineno)
                print("before extract min vertex_iter=", vertex_iter)
                print("bmh is heap=", self._bmh.is_heap())
                print("bmh is valid", self._bmh.has_valid_heap_and_map())
                print("bmh vertecies=", self._bmh.vertex_keys)
                print("bmh values=", self._bmh.vertex_values)
                print("bmh = ", self._bmh)
                print("***********************************************")
            key, value = self._bmh.extract_min()
            self._distances[key] = value
            if verbose:
                print("\n\n***********************************************")
                print("line = ", inspect.currentframe().f_back.f_lineno)
                print("after extract min vertex_iter=", vertex_iter)
                print("key=", key, " value=", value)
                print("adjacent_keys=", self._graph.adjacent_verticies(key))
                print("bmh is heap=", self._bmh.is_heap())
                print("bmh is valid", self._bmh.has_valid_heap_and_map())
                print("bmh = ", self._bmh)
                print("***********************************************")
            if edge_iter == 0:
                self._parents[key] = []
            for adj_key in self._graph.adjacent_verticies(key):
                if verbose:
                    print("    line = ", inspect.currentframe().f_back.f_lineno)
                    print("    adj_key = ", adj_key, " key=", key)
                    print("    bmh has key = ", self._bmh.contains_vertex_key(adj_key))
                    print("    bmh is heap = ", self._bmh.is_heap())
                    print("    bmh is valid= ", self._bmh.has_valid_heap_and_map())
                    print("    bmh = ", self._bmh)
                edge_weight = self._graph.get_edge_weight(key, adj_key)
                if verbose:
                    print("    edge_weight = ", edge_weight)
                if self._bmh.contains_vertex_key(adj_key):
                    if verbose and not self._bmh.has_valid_heap_and_map():
                        print( "invalid heap and map at edge_iter=", edge_iter)
#                    if vertex_iter == 2:
#                        pdb.set_trace()
                    adj_value = self._bmh.get_value(adj_key)
                    test_dist = value + edge_weight
                    if test_dist < adj_value:
                        if verbose:
                            print("    before decrease key")
                            print("    line = ", inspect.currentframe().f_back.f_lineno)
                            print("    adj_key=", adj_key, " key=", key)
                            print("    bmh is heap=", self._bmh.is_heap())
                            print("    bmh is valid=", self._bmh.has_valid_heap_and_map())
                            print("    bmh = ", self._bmh)
                        self._parents[adj_key] = [key]
                        self._bmh.decrease_value(adj_key, test_dist)
                        if verbose:
                            print("    after decrease key")
                            print("    line = ", inspect.currentframe().f_back.f_lineno)
                            print("    adj_key=", adj_key, " key=", key)
                            print("    bmh is heap=", self._bmh.is_heap())
                            print("    bmh is valid=", self._bmh.has_valid_heap_and_map())
                            print("    bmh = ", self._bmh)
                            if not self._bmh.has_valid_heap_and_map():
                                print( "giving up", adj_key)
                                raise ValueError("corrupt heap")
                    elif test_dist == value:
                        self._parents[adj_key].append(key)
                edge_iter = edge_iter + 1
            vertex_iter = vertex_iter + 1


    def get_parent(self, vertex_id):
        ''' Returns parents of vertex_id '''
        if not vertex_id in self._parents:
            raise ValueError("vertex id not found")
        else:
            return self._parents[vertex_id]


    @property
    def parents(self):
        return self._parents


    @property
    def distances(self):
        return self._distances
