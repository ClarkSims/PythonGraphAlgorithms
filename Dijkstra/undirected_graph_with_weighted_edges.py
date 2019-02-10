#!/usr/bin/env python3
''' class for representing undireted graph with weighted edges '''
#import pdb

class UndirectedGraphWithWeightedEdges:
    ''' class for representing an undirected graph with weighted edges '''
    def __init__(self, verticies=None, edge_weights=None, reverse_keys=False):
        ''' init function, note that verticies and edge_weights both passed by reference '''
        # define verticies
        if not verticies is None:
            if isinstance(verticies, set):
                self._verticies = verticies
            else:
                self._verticies = set(verticies)
        else:
            self._verticies = set()
        # define empty set of adjacent verticies, will fill later
        self._adjacent_verticies = {}
        #define edge_weights, adjacent_verticies is derived from these
        if not edge_weights is None:
            if isinstance(edge_weights, dict):
                self._edge_weights = edge_weights
            else:
                raise ValueError("edge_weights must be a dict")
            for vertex in verticies:
                self._adjacent_verticies[vertex] = set()
            for edge, weight in edge_weights.items():
                self.validate_edge_weight_sync_verticies(edge, weight, reverse_keys)
        else:
            self._edge_weights = {}


    def empty(self):
        ''' returns True for empty heap '''
        return not self._verticies


    @property
    def verticies(self):
        ''' returns verticies '''
        return self._verticies


    @property
    def edge_weights(self):
        ''' returns edge_weights '''
        return self._edge_weights


    def adjacent_verticies(self, vertex):
        ''' returns list of adjacent verticies '''
        if vertex not in self._adjacent_verticies:
            raise ValueError("vertex={} not in graph".format(vertex))
        return self._adjacent_verticies[vertex]


    @property
    def number_verticies(self):
        ''' returns number of verticies '''
        return len(self._verticies)


    @property
    def number_edges(self):
        ''' returns number of verticies '''
        return len(self._edge_weights)


    def _add_vertex(self, vertex):
        ''' add vertex without validation '''
        self._verticies.add(vertex)
        self._adjacent_verticies[vertex] = set()


    def _add_edge_weight(self, edge, weight):
        ''' add edge_weight without validation '''
        self._edge_weights[edge] = weight

    def validate_edge_weight_sync_verticies(self, raw_edge, weight, reverse_keys=False):
#        if raw_edge == ('f', 'c'):
#            pdb.set_trace()
        ''' add edge and weight, validate both, add verticies if missing '''
        if len(raw_edge) != 2:
            raise ValueError("length raw_edge weight != 2 for raw_edge={}".format(raw_edge))
        if raw_edge[0] >= raw_edge[1]:
            if reverse_keys:
                edge = (raw_edge[1],raw_edge[0])
                if raw_edge in self._edge_weights:
                    weight = self._edge_weights[raw_edge]
                    self._edge_weights.pop(raw_edge)
                    self._edge_weights[edge] = weight
            else:
                raise ValueError("ew[0] >= ew[1], raw_edge={}".format(raw_edge))
        else:
            edge = raw_edge
        if weight < 0:
            raise ValueError("weight<0 weight={} edge={}".format(weight, edge))
        if edge[0] not in self._verticies:
            self._add_vertex(edge[0])
        if edge[1] not in self._verticies:
            self._add_vertex(edge[1])
        self._adjacent_verticies[edge[0]].add(edge[1])
        self._adjacent_verticies[edge[1]].add(edge[0])


    def add_edge_weight(self, raw_edge, weight):
        ''' add edge_weight with validation '''
        if raw_edge[0] > raw_edge[1]:
            edge = (raw_edge[1],raw_edge[0])
            pdb.set_trace()
        else:
            edge = raw_edge
        self.validate_edge_weight_sync_verticies(edge, weight)
        if edge in self._edge_weights:
            raise ValueError("edge={} already in edge weights".format(edge))
        self._add_edge_weight(edge, weight)


    def create_and_add_edge_weight(self, vrtx0, vrtx1, weight):
        ''' create edge and weight, validate everything '''
        if vrtx0 == vrtx1:
            raise ValueError("vrtx0==vrtx1 = {} in add_edge_weight".format(vrtx1))
        if vrtx0 > vrtx1:
            vrtx1, vrtx0 = vrtx0, vrtx1
        if weight < 0:
            raise ValueError("weight={}<0 in create_and_add_edge_weight".format(weight))
        if not vrtx0 in self._verticies:
            self._add_vertex(vrtx0)
        if not vrtx1 in self._verticies:
            self._add_vertex(vrtx1)
        edge = (vrtx0, vrtx1)
        if edge in self._edge_weights:
            raise ValueError("edge={} already in edge weights".format(edge))
        self._add_edge_weight(edge, weight)


    def get_edge_weight(self, vrtx0, vrtx1):
        if vrtx0 == vrtx1:
            raise ValueError("vrtx0==vrtx1 = {} in add_edge_weight".format(vrtx1))
        if vrtx0 > vrtx1:
            vrtx1, vrtx0 = vrtx0, vrtx1
        edge = (vrtx0, vrtx1)
        if edge in self._edge_weights:
            return self._edge_weights[edge]


    def is_valid(self):
        for edge, weight in self._edge_weights.items():
            if edge[0] >= edge[1]:
                print("edge[0] >= edge[1], edge=", edge)
                return False
            elif weight < 0:
                print("weight < 0, weight=", weight)
                return False
            elif edge[0] not in self._adjacent_verticies:
                print("edge[0] not in self._adjacent_verticies, edge=", edge)
                return False
            elif edge[1] not in self._adjacent_verticies:
                print("edge[1] not in self._adjacent_verticies, edge=", edge)
                return False
            elif edge[0] not in self._verticies:
                print("edge[0] not in self._verticies, edge=", edge)
                return False
            elif edge[1] not in self._verticies:
                print("edge[1] not in self._verticies, edge=", edge)
                return False
        return True
