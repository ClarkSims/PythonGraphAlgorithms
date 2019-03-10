#!/usr/bin/env python3
import topological_sort as ts
import unittest

class TestTopologicalSort(unittest.TestCase):
    def test_line(self):
        dag = {0 : [1], 1 : [2], 2 : [3], 3 : []}
        top_dependencies = []
        dependencies = ts.topological_sort(dag, top_dependencies)
        self.assertEqual([3, 2, 1, 0], dependencies)
        self.assertEqual([3], top_dependencies)


    def test_two_parents(self):
        dag = {0 : [1, 2], 1 : [], 2 : []}
        top_dependencies = []
        dependencies = ts.topological_sort(dag, top_dependencies)
        self.assertEqual([2, 1, 0], dependencies)
        self.assertEqual([1, 2], top_dependencies)


    def test_diamond(self):
        dag = {0 : [1, 2], 1 : [3], 2 : [3], 3 : []}
        top_dependencies = []
        dependencies = ts.topological_sort(dag, top_dependencies)
        self.assertEqual([3, 2, 1, 0], dependencies)
        self.assertEqual([3], top_dependencies)


    def test_cycle(self):
        dag = {0 : [1], 1 : [2], 2 : [0]}
        top_dependencies = []
        with self.assertRaises(IndexError):
            ts.topological_sort(dag, top_dependencies)


if __name__ == '__main__':
    unittest.main() 
