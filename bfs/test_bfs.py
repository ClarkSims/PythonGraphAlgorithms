#!/usr/bin/env python3
import bfs
import unittest

class TestSimpleBreadthFirstSearch(unittest.TestCase):
    def test_two(self):
        graph = {0 : [1, 2], 1 : [3], 2 : [4], 3 : [], 4 : []}
        path_len = bfs.simple_breadth_first_search(graph, 0, 3)
        self.assertEqual(2, path_len)


class TestDoubleBreadthFirstSearch(unittest.TestCase):
    def test_two(self):
        graph = {0 : [1, 2], 1 : [3], 2 : [4], 3 : [], 4 : []}
        path_len = bfs.simple_breadth_first_search(graph, 0, 3)
        self.assertEqual(2, path_len)


if __name__ == '__main__':
    unittest.main() 
