#!/usr/bin/env python3
'''
test suite for binary heap map
'''
import unittest
import pdb
import math
from binary_min_heap_map import *
#import pdb

class TestAddToHeap(unittest.TestCase):
    def test_trivial_add_to_heap(self):
        bmh = BinaryMinHeapMap()

        self.assertTrue(bmh.empty)
        self.assertEqual(bmh.heap_size, 0)

        bmh.add_to_heap(1, 1)

        self.assertFalse(bmh.empty)
        self.assertEqual(bmh.heap_size, 1)

    def test_two_level_add_to_heap_permutation1(self):
        bmh = BinaryMinHeapMap()
        self.assertTrue(bmh.empty)
        self.assertEqual(bmh.heap_size, 0)
        bmh.add_to_heap(1, 9)
        self.assertTrue(bmh.contains_vertex_key(1))
        self.assertEqual(bmh.vertex_values, [9])
        self.assertEqual(bmh.vertex_keys, [1])
        bmh.add_to_heap(2, 8)
        self.assertEqual(bmh.vertex_values, [8, 9])
        self.assertEqual(bmh.vertex_keys, [2, 1])
        self.assertTrue(bmh.contains_vertex_key(1))
        self.assertTrue(bmh.contains_vertex_key(2))
        bmh.add_to_heap(3, 7)
        self.assertEqual(bmh.vertex_values, [7, 9, 8])
        self.assertEqual(bmh.vertex_keys, [3, 1, 2])
        self.contains_123(bmh)


    def test_two_level_add_to_heap_permutation3(self):
        bmh = BinaryMinHeapMap()
        self.assertTrue(bmh.empty)
        self.assertEqual(bmh.heap_size, 0)
        bmh.add_to_heap(1, 9)
        self.assertEqual(bmh.vertex_values, [9])
        self.assertEqual(bmh.vertex_keys, [1])
        bmh.add_to_heap(3, 7)
        self.assertEqual(bmh.vertex_values, [7, 9])
        self.assertEqual(bmh.vertex_keys, [3, 1])
        bmh.add_to_heap(2, 8)
        self.assertEqual(bmh.vertex_values, [7, 9, 8])
        self.assertEqual(bmh.vertex_keys, [3, 1, 2])
        self.contains_123(bmh)


    def contains_123(self, bmh):
        self.assertTrue(bmh.contains_vertex_key(1))
        self.assertTrue(bmh.contains_vertex_key(2))
        self.assertTrue(bmh.contains_vertex_key(3))


class TestCreationOfBinaryHeapMap(unittest.TestCase):
    def test_create_empty(self):
        bmh = BinaryMinHeapMap()
        self.assertTrue(bmh.empty)


    def test_raise_execptions(self):
        self.assertRaises(ValueError, BinaryMinHeapMap, vertex_keys = range(0, 10))
        self.assertRaises(ValueError, BinaryMinHeapMap, vertex_keys = range(0, 10), 
            vertex_values=range(0,5))


    def test_init_with_list(self):
        N = 10
        vertex_keys = range(0, N)
        vertex_values = range(0, N)
        bmh = BinaryMinHeapMap(vertex_keys=vertex_keys, vertex_values=vertex_values)
        for i in range(0, N):
            self.assertEqual(i, bmh.get_value(i))
        bmh.heap[0].value = 100
        self.assertFalse(bmh.is_heap())


class TestChangeHeap(unittest.TestCase): 
    def test_decrease_value(self):
        bmh = BinaryMinHeapMap()
        N = 10
        bmh._init_without_heapify(range(0, N), range(0, N))
        self.assertTrue(bmh.is_heap())
        for i in range(1, N):
            bmh.decrease_value(i, -i)
            self.assertTrue(bmh.is_heap())
            self.assertEqual(-i, bmh.get_value(i))
            nd = bmh.heap[0]
            self.assertEqual(i, nd.key)
            self.assertEqual(-i, nd.value)
        self.assertRaises( ValueError, bmh.decrease_value, 1000, 0)
        self.assertRaises( ValueError, bmh.decrease_value, -100, 1000)


    class TestExtractMin(unittest.TestCase):
        def test_trivial_extract_min(self):
            ''' testing sorted range '''
            bmh = BinaryMinHeapMap()
            N = 10
            bmh._init_without_heapify(range(0, N), range(0, N))
            self.assertTrue(bmh.is_heap())
            for i in range(0, N):
                vertex_key, vertex_value = bmh.extract_min()
                self.assertTrue(bmh.is_heap())
                self.assertEqual(i, vertex_key)
                self.assertEqual(i, vertex_value)


        def test_dijkstra_failure(self):
            ''' testing case that failed in Dijstra's algorithm '''
            vertex_keys =   ['b', 'f', 'c', 'd', 'e'] 
            vertex_values = [2, 4, math.inf, 5, math.inf]
            bmh = BinaryMinHeapMap(vertex_keys, vertex_values)
            self.assertTrue(bmh.is_heap())
            self.assertTrue(bmh.has_valid_heap_and_map())

            vertex_key, vertex_value = bmh.extract_min()
            self.assertEqual('b', vertex_key)
            self.assertEqual(2, vertex_value)
            self.assertTrue(bmh.is_heap())
            self.assertTrue(bmh.has_valid_heap_and_map())


class TestHeapSort(unittest.TestCase):
    def test_heap_sort(self):
        '''test sort'''
        rand_vals=[9,7,8,6,4,5,1,2,3,0]
        sorted_input=rand_vals[:]
        sorted_input.sort()
        heap_input=rand_vals[:]
        heap_sorted_vals=[]
        bmh = BinaryMinHeapMap(vertex_keys=range(10), vertex_values=heap_input)
        for i in range(10):
            self.assertTrue(not bmh.empty)
            new_min = bmh.heap[0].value
            self.assertEqual(i, new_min)
            bmh.extract_min()
            self.assertTrue(bmh.is_heap())
            heap_sorted_vals.append(new_min)
        self.assertEqual(sorted_input,heap_sorted_vals)


if __name__ == "__main__":
    unittest.main()
