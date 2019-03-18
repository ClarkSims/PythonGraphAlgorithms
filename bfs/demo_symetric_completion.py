#!/usr/bin/env python3
from symmetric_completion import symmetric_completion as sc
from bfs import double_sided_breadth_first_search as dsbfs

def main():
    dg = {0 : [1], 1 : [2], 2 : [3], 3 : [4], 4 : [0]}
    ug = sc(dg)
    print("directed graph = ", dg)
    print("undirected graph = ", ug)
    dist = dsbfs(dg, 0, 2) 
    print("distance between 0 and 2 is ", dist)
 

if __name__ == '__main__':
    main()

