#!/usr/bin/env python3
'''Demonstration of the the functions in topological_sort.py'''
import topological_sort as ts

def demo_func():
    '''Demonstration of the the functions in topological_sort.py'''
    dag = {0 : [1], 1 : [2], 2 : [3], 3 : []}
    top_dependencies = []
    dependencies = ts.topological_sort(dag, top_dependencies)
    print("demo 1")
    print("dependencies = ", dependencies)
    print("top_dependencies = ", top_dependencies)

    dag = {0 : [1, 2], 1 : [], 2 : []}
    top_dependencies = []
    dependencies = ts.topological_sort(dag, top_dependencies)
    print("demo 2")
    print("dependencies = ", dependencies)
    print("top_dependencies = ", top_dependencies)

    dag = {0 : [1, 2], 1 : [3], 2 : [3], 3 : []}
    top_dependencies = []
    dependencies = ts.topological_sort(dag, top_dependencies)
    print("demo 3")
    print("dependencies = ", dependencies)
    print("top_dependencies = ", top_dependencies)


if __name__ == '__main__':
    demo_func()
