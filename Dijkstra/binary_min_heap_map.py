#!/usr/bin/env python3
'''
    Module which implements a container for Prim's and Dijkstra's algoritms.
'''

import pdb

class BinaryMinHeapMap:
    """Binary Heap and Map for implementing Dijkstra's and Prim's algorithms

    This class supports the functions necessary to implement Dijkstra's and Prim's algorithms:
    extract_min              - O(logn)
    add_to_heap               - O(logn)
    contains_vertex_key        - O(1)
    decrease_value - O(logn)
    get_value      - O(1)
    size                    - O(1)
    empty                   - O(1)
    filter_up                - O(log(n))
    filter_down              - O(log(n))

    """
    class Node:
        """ Represent combination of node id and value """
        def __init__(self, vertex_key, value):
            self.key = vertex_key
            self.value = value


        def __repr__(self):
            return "(id={} value={})".format(self.key, self.value)

    def __repr__(self):
        return "heap={} map={}".format(self.heap, self.map)

    def is_heap(self):
        """ checks that the heap condition is true for all nodes """
        for vertex_offset in reversed(range(1, len(self.heap))):
            parent_offset = (vertex_offset - 1) // 2
            vertex_value = self.heap[vertex_offset].value
            parent_value = self.heap[parent_offset].value
            if parent_value > vertex_value:
                return False
        return True


    def _init_without_heapify(self, vertex_keys, vertex_values):
        if len(vertex_values) != len(vertex_keys):
            raise ValueError("len(vertex_values) != len(vertex_keys)")
        self.heap = [BinaryMinHeapMap.Node(vid, val) for vid, val in \
            zip(vertex_keys, vertex_values)]
        self.map = {vid : i for vid, i in zip(vertex_keys, range(0, len(vertex_keys)))}


    def __init__(self, vertex_keys=None, vertex_values=None):
        if vertex_keys is not None:
            if not vertex_values:
                raise ValueError("vertex_values is None, while vertex_keys is not None")
            self._init_without_heapify(vertex_keys, vertex_values)
            for i in reversed(range(0, len(vertex_keys) // 2)):
                self.filter_down(i)
        else:
            self.map = {}
            self.heap = []


    def add_to_heap(self, vertex_key, vertex_value):
        """adds Node(vertex_key, vertex_value) to self.heap and self.map, then filters up"""
        vertex_offset = len(self.heap)
        self.heap.append(BinaryMinHeapMap.Node(vertex_key, vertex_value))
        self.map[vertex_key] = vertex_offset
        self.filter_up(vertex_offset)


    def filter_up(self, vertex_offset):
        """ Moves Node at vertex_offset, up, until MinHeap property is satisfied, updates map """
        initial_vertex_offset = vertex_offset
        node = self.heap[vertex_offset]
        vertex_key = node.key
        parent_offset = (vertex_offset - 1) // 2
        while parent_offset >= 0:
            parent_node = self.heap[parent_offset]
            parent_key = parent_node.key
            parent_value = parent_node.value
            if parent_value < node.value:
                break
            else:
                self.map[parent_key] = vertex_offset
                self.heap[vertex_offset] = parent_node
                vertex_offset = parent_offset
                parent_offset = (vertex_offset - 1) // 2
        if initial_vertex_offset != vertex_offset:
            self.map[vertex_key] = vertex_offset
            self.heap[vertex_offset] = node


    def filter_down(self, vertex_offset):
        ''' moves value at location to new location farther down '''
        node = self.heap[vertex_offset]
        child_offset = 2*vertex_offset + 1
        heap_length = len(self.heap)
        while child_offset < heap_length:
            if child_offset < heap_length-1 and \
                self.heap[child_offset + 1].value < self.heap[child_offset].value:
                child_offset = child_offset + 1
            child_node = self.heap[child_offset]
            if node.value > child_node.value:
                self.map[child_node.key] = vertex_offset
                self.heap[vertex_offset], self.heap[child_offset] = child_node, node
            else:
                break
            vertex_offset = child_offset
            child_offset = 2*vertex_offset + 1
        self.map[node.key] = vertex_offset
        return vertex_offset


    def contains_vertex_key(self, vertex_key):
        ''' returns true if vertex specified by key is in map '''
        return vertex_key in self.map


    def decrease_value(self, vertex_key, vertex_value):
        """changes value of vertex, with vertex_key, maintains heap ordering"""
        if not vertex_key in self.map:
            raise ValueError("vertex_key={} not in _map".format(vertex_key))
        vertex_offset = self.map[vertex_key]
        node = self.heap[vertex_offset]
        if node.value <= vertex_value:
            raise ValueError("previous node value={} <= new value = {} ".format(
                node.value, vertex_value))
        node.value = vertex_value
        self.filter_up(vertex_offset)


    def extract_min(self):
        '''returns minimum of heap, removes from heap, adjust heap accordingly'''
        heap_len = len(self.map)
        if heap_len == 0:
            raise ValueError("extract_min called on empty BinearyMinHeapMap")
        node = self.heap[0]
        self.map.pop(node.key)
        if heap_len > 1:
            self.heap[0] = self.heap.pop() # put last node as first
            self.map[self.heap[0].key] = 0
#            if not self.has_valid_heap_and_map():
#                raise RuntimeError("heap invalid after shift")
#            pdb.set_trace()
            self.filter_down(0)
#            if not self.has_valid_heap_and_map():
#                raise RuntimeError("heap invalid after filterdown")
        elif heap_len == 1:
            self.heap.pop()
        return (node.key, node.value)


    def get_value(self, vertex_key):
        ''' returns value of vertex with key = vertex_key'''
        if not vertex_key in self.map:
            raise ValueError("vertex_key={} in self.map".format(vertex_key))
        vertex_offset = self.map[vertex_key]
        if len(self.heap) != len( self.map ):
            print("self.heap) != len( self.map)" )
            pdb.set_trace()
        if vertex_offset >= len(self.heap):
            print("vertex_offset >= len(self.heap)")
            pdb.set_trace()
        return self.heap[vertex_offset].value


    def has_valid_heap_and_map(self):
        ''' checks that heap and map are consistant '''
        if len(self.heap) != len( self.map ):
            print("self.heap) != len( self.map)" )
            return False
        for key, offset in self.map.items():
            if offset < 0 or offset >= len(self.heap):
                print("offset < 0 or offset >= len(self.heap)")
                return False
            if self.heap[offset].key != key:
                print("self.heap[offset].key != key, offset=", offset, " key=", key)
                return False
        return True


    @property
    def heap_size(self):
        ''' returns number of items in heap '''
        return len(self.heap)


    @property
    def empty(self):
        ''' returns True for empty heap '''
        return not self.heap


    @property
    def vertex_values(self):
        ''' returns list of vertex values '''
        return [node.value for node in self.heap]


    @property
    def vertex_keys(self):
        ''' returns list of vertex keys '''
        return [node.key for node in self.heap]
