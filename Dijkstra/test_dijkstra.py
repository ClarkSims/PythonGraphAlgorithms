#!/usr/bin/env python3
'''
test suite for dijkstra
'''
import unittest
import pdb
from dijkstra import Dijkstra
#import pdb

class TestDijkstraOptimum(unittest.TestCase):
#    @unittest.skip
    def test_empty_init(self):
        ''' empty init '''
        djk = Dijkstra()
        self.assertRaises(ValueError, djk.iterate)
        self.assertTrue(not djk.parents)
        self.assertEqual({}, djk.distances)


#    @unittest.skip
    def test_one_point(self):
        ''' test simple 1 point '''
        start_vertex = 0
        verticies = [0]
        edge_weights = {}
        djk = Dijkstra( start_vertex, verticies, edge_weights)
        djk.iterate()
#        self.assertRaises(ValueError, djk.iterate)
        self.assertEqual(1, len(djk.parents)) #parents is empty
        self.assertEqual([], djk.parents[0])
        self.assertEqual({0:0}, djk.distances)


 #   @unittest.skip
    def test_two_point(self):
        ''' test simple 2 point '''
        start_vertex = 0
        verticies = [0,1]
        edge_weights = {(0,1) : 1}
        djk = Dijkstra( start_vertex, verticies, edge_weights)
#        pdb.set_trace()
        djk.iterate()
#        self.assertRaises(ValueError, djk.iterate)
#        print( "parents=", djk.parents)
        self.assertEqual(2, len(djk.parents)) #parents is empty
        self.assertEqual([], djk.parents[0])
        self.assertEqual([0], djk.parents[1])
        self.assertEqual({0:0, 1:1}, djk.distances)


    def test_three_point_a(self):
        ''' test simple 3 point '''
        start_vertex = 0
        verticies = [0,1,2]
        edge_weights = {(0,1) : 1, (0,2) : 1}
        djk = Dijkstra( start_vertex, verticies, edge_weights)
#        pdb.set_trace()
        djk.iterate()
#        self.assertRaises(ValueError, djk.iterate)
#        print( "parents=", djk.parents)
        self.assertEqual(3, len(djk.parents)) #parents is empty
        self.assertEqual([], djk.parents[0])
        self.assertEqual([0], djk.parents[1])
        self.assertEqual([0], djk.parents[2])
        self.assertEqual({0:0, 1:1, 2:1}, djk.distances)


    def test_three_point_b(self):
        ''' test simple 3 point '''
        start_vertex = 0
        verticies = [0,1,2]
        edge_weights = {(0,1) : 1, (1,2) : 2}
        djk = Dijkstra( start_vertex, verticies, edge_weights)
#        pdb.set_trace()
        djk.iterate()
#        self.assertRaises(ValueError, djk.iterate)
#        print( "parents=", djk.parents)
        self.assertEqual(3, len(djk.parents)) #parents is empty
        self.assertEqual([], djk.parents[0])
        self.assertEqual([0], djk.parents[1])
        self.assertEqual([1], djk.parents[2])
        self.assertEqual({0:0, 1:1, 2:3}, djk.distances)


    def test_four_point_a(self):
        ''' test simple 4 point '''
        start_vertex = 0
        verticies = [0,1,2,3]
        edge_weights = {(0,1) : 1, (0,2) : 1, (1,3):1, (2,3) : 2}
        djk = Dijkstra( start_vertex, verticies, edge_weights)
#        pdb.set_trace()
        djk.iterate()
#        self.assertRaises(ValueError, djk.iterate)
#        print( "parents=", djk.parents)
        self.assertEqual(4, len(djk.parents)) #parents is empty
        self.assertEqual([], djk.parents[0])
        self.assertEqual([0], djk.parents[1])
        self.assertEqual([0], djk.parents[2])
        self.assertEqual([1], djk.parents[3])
        self.assertEqual({0:0, 1:1, 2:1, 3:2}, djk.distances)

    def test_tushar_roy(self):
        ''' example from Tushar Roy's video https://www.youtube.com/watch?v=lAXZGERcDf4 '''
        start_vertex = 'a'
        verticies = ['a','b','c','d','e','f']
#       edge_weights = {('a','b') : 2, ('a','f') : 4, ('a','d'):5, ('b','c') : 4, ('f','c') : 3, ('f','d') : 2, ('d','e') : 1}
        edge_weights = {('a','b') : 2, ('a','f') : 4, ('a','d'):5, ('b','c') : 4, ('c','f') : 3, ('d','f') : 2, ('d','e') : 1}
        djk = Dijkstra( start_vertex, verticies, edge_weights)
#        pdb.set_trace()
        djk.iterate()
#        self.assertRaises(ValueError, djk.iterate)
#        print( "parents=", djk.parents)
        self.assertEqual(6, len(djk.parents)) #parents is empty
#        print( "parents=", djk.parents)
        self.assertEqual([], djk.parents['a'])
        self.assertEqual(['a'], djk.parents['b'])
        self.assertEqual(['a'], djk.parents['d'])
        self.assertEqual(['a'], djk.parents['f'])
        self.assertEqual(['b'], djk.parents['c'])



if __name__ == "__main__":
    unittest.main()
