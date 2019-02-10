#!/usr/bin/env python3
''' unit test for undirected_graph_with_weighted_edges '''
import unittest
from undirected_graph_with_weighted_edges import UndirectedGraphWithWeightedEdges
#import pdb

class TestUndirectedGraphWithWeightedEdges(unittest.TestCase):
    '''test cases for __init__'''
    def test_empty_init(self):
        ''' empty init '''
        und_gr = UndirectedGraphWithWeightedEdges()
        self.assertTrue(und_gr.empty())
        self.assertEqual(0, und_gr.number_verticies)
        self.assertEqual(0, und_gr.number_edges)


    def test_init_with_data(self):
        ''' pass data to init '''

        #create circular array, 10 verticies, 2 neighbors for each vertex
        num = 10
        verticies = list(range(0, num))
        edge_weights = {}
        for i in range(1, num):
            prev_i = i-1
            edge_weights[(prev_i, i)] = 1
        edge_weights[(0, num-1)] = 1
        und_gr = UndirectedGraphWithWeightedEdges(verticies=verticies, edge_weights=edge_weights)
        self.assertEqual(num, und_gr.number_verticies)
        self.assertEqual(num, und_gr.number_edges)
        self.assertEqual(edge_weights, und_gr.edge_weights)
        for vertex in verticies:
            self.assertEqual(2, len(und_gr.adjacent_verticies(vertex)))
        self.assertTrue(und_gr.is_valid())

        #same test, use set instead of list
        verticies = set(verticies)
        und_gr2 = UndirectedGraphWithWeightedEdges(verticies=verticies, edge_weights=edge_weights)
        self.assertEqual(num, und_gr2.number_verticies)
        self.assertEqual(num, und_gr2.number_edges)
        self.assertTrue(und_gr2.is_valid())

        #test validation: check edge weight > 0
        edge_weights[(0, 1)] = -1
        self.assertRaises(ValueError, UndirectedGraphWithWeightedEdges, \
            verticies=verticies, edge_weights=edge_weights)
        edge_weights[(0, 1)] = 1

        #test validation: check tuple length==2
        edge_weights[(0, 1, 2)] = 1
        self.assertRaises(ValueError, UndirectedGraphWithWeightedEdges, \
            verticies=verticies, edge_weights=edge_weights)
        edge_weights.pop((0, 1, 2))

        #test validation: check addition of missing verticies
        edge_weights[(0, 100)] = 1
        und_gr3 = UndirectedGraphWithWeightedEdges(verticies=verticies, edge_weights=edge_weights)
        self.assertTrue(100 in  und_gr3.verticies)
        self.assertTrue(und_gr3.is_valid())

        #fix reference for edge_weights
        edge_weights.pop((0, 100))
        self.assertTrue(und_gr.is_valid())

        #test validation: check edge_weights is dict
        self.assertRaises(ValueError, UndirectedGraphWithWeightedEdges, \
            verticies=verticies, edge_weights=list())

        #check add individual edge
        und_gr.add_edge_weight((0, 5), 2)
        self.assertEqual(3, len(und_gr.adjacent_verticies(5)))
        self.assertEqual(3, len(und_gr.adjacent_verticies(0)))
        self.assertTrue(und_gr.is_valid())

        #check invalid request for adjacent vertecies
        self.assertRaises(ValueError, und_gr.adjacent_verticies, 100)

        #reverse order for edge
        self.assertRaises(ValueError, und_gr.validate_edge_weight_sync_verticies, (9, 0), 1)

        #test error catching, add missing vertex
        self.assertRaises(ValueError, und_gr.create_and_add_edge_weight, 0, 5, -1)
        und_gr.validate_edge_weight_sync_verticies((-1, 0), 1)
        self.assertTrue(und_gr.is_valid())


#    @unittest.skip
    def test_tushar_roy(self):
        verticies = ['a','b','c','d','e','f']
        edge_weights = {('a','b') : 2, ('a','f') : 4, ('a','d'):5, ('b','c') : 4, ('f','c') : 3, ('f','d') : 2, ('d','e') : 1}
        und_gr = UndirectedGraphWithWeightedEdges(verticies=verticies, edge_weights=edge_weights, reverse_keys=True)
        self.assertTrue(und_gr.is_valid())


    def test_build_incrementally(self):
        ''' test building graph edge by edge '''
        und_gr = UndirectedGraphWithWeightedEdges()
        num = 10
        for i in range(1, num):
            und_gr.create_and_add_edge_weight(i-1, i, 1)
        und_gr.create_and_add_edge_weight(num-1, 0, 1)
        self.assertEqual(num, und_gr.number_verticies)
        self.assertEqual(num, und_gr.number_edges)

        #test automatically adding new vertex
        und_gr.add_edge_weight((0, 100), 1)
        self.assertTrue(und_gr.is_valid())

        #test error catching, negative weight
        self.assertRaises(ValueError, und_gr.create_and_add_edge_weight, 0, 5, -1)

        #test error catching, circular edge
        self.assertRaises(ValueError, und_gr.create_and_add_edge_weight, 0, 0, 1)

        #test error catching, same edge twice
        self.assertRaises(ValueError, und_gr.create_and_add_edge_weight, 0, 9, 1)
        self.assertRaises(ValueError, und_gr.add_edge_weight, (0, 9), 1)


if __name__ == "__main__":
    unittest.main()
