#!/usr/bin/env python3
import tsp
import unittest
import pdb

def make_circular_graph(N):
    graph = {}
    dist = {}
    for i in range(1,N):
        graph[i] = [i+1]
        dist[(i, i+1)] = 1
    #final edge, to close circle
    graph[N] = [1]
    dist[(N, 1)] = 1
    return graph, dist


class TestCircles(unittest.TestCase):
    def test_one_point(self):
        graph = {1 : []}
        dist = {}
        cost, parents = tsp.traveling_salesman_problem(graph, dist)
        self.assertEqual(0, len(cost))
        self.assertEqual(0, len(parents))


    def test_two_points_circle(self):
        graph = {1 : [2],  2 : [1]}
        dist = { (1, 2) : 1, (2, 1) : 1 }
        cost, parents = tsp.traveling_salesman_problem(graph, dist)
        self.assertEqual(1, len(cost))
        self.assertEqual(2, len(parents))


    def test_three_points_circle(self):
        graph = {1 : [2],  2 : [3], 3 : [1]}
        dist = { (1, 2) : 1, (2, 3) : 1, (3, 1) : 1}
        cost, parents = tsp.traveling_salesman_problem(graph, dist)
        self.assertEqual(1, len(cost))
        self.assertEqual(3, len(parents))


    def test_N_points_circle(self):
        for N in range(2,20):
            graph, dist = make_circular_graph(N)
            cost, parents = tsp.traveling_salesman_problem(graph, dist)
            self.assertEqual(1, len(cost))
            self.assertEqual(N, len(parents))
        

class TestEmbededCircles(unittest.TestCase):
    def test_three_points_embedded_circle(self):
        graph = {1 : [2, 3],  2 : [3, 1], 3 : [1, 2]}
        dist = { (1, 2) : 1, (2, 3) : 1, (3, 1) : 1, (1, 3) : 2, (3, 2) : 2}
        all_cost, parents = tsp.traveling_salesman_problem(graph, dist)
#        print("all_cost={", end="")
#        tsp.print_path_and_cost(all_cost)
#        print("\n}")
        self.assertEqual(1, len(all_cost))
        self.assertEqual(3, len(parents))


if __name__ == '__main__':
    unittest.main()

