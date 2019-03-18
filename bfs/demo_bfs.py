#!/usr/bin/env python3
import bfs
import pdb

def main():
    graph = {0 : [1, 2], 1 : [3], 2 : [4], 3 : [], 4 : []}
    path_len = bfs.simple_breadth_first_search(graph, 0, 3)
    print("path_len = ", path_len)
#    pdb.set_trace()
    path_len = bfs.double_sided_breadth_first_search(graph, 0, 3)
    print("path_len = ", path_len)

if __name__ == '__main__':
    main()
