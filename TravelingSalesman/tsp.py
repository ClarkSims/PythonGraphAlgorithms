'''Traveling Salesman Problem
This module implements a more efficient version the Held Karp algorithm for
solving the Anti-Symetric Traveling Salesman Problem.
https://en.wikipedia.org/wiki/Travelling_salesman_problem
https://en.wikipedia.org/wiki/Held%E2%80%93Karp_algorithm
This is a bottom up implementation, which only looks at permutations of
verticies that arise from following edges with finite weight. In the
standard implementation, all permutations of the power set of all verticies
is explored, and edges which do not exist, are substutitued with an edge
of infinite weight.
I based this code on Tushar Roy's soltion for the TSP, https://github.com/mission-peace/interview/blob/master/src/com/interview/graph/TravelingSalesmanHeldKarp.java, 
and unwittlingly copied a design error. He stores the parent pointers, in a container that maps vertex to vertex. This does not allow allow enumeration of multiple paths,
if there are multiple minimum solutions. However this is still wrong.
The parent pointers should be stored in a map, from the mnemonics to mnemonics,
since each parent pointer represents a transition from one mnemonic to another.
In this case, the map reduces to a map of nmenomic to vertex list, since each
successive mnemonic in the path, can be represented as a set of interternal verticies,
and the final vertex, (see class Path). On needs as the domain, a full path, and as the range,
the set of vericies, which are paths one shorter in length, which end in the respective
vertex.
'''
import copy
import pdb

def print_path_and_cost(cost_dict):
    for path, cost in cost_dict.items():
        print( "{{{} : {}}}".format(path, cost), end=", ")

def traveling_salesman_problem(graph, dist, vertex0=None, verbose=False):
    ''' An optimized version of the Held Karp algorithm for solving the TSP
        graph : a graph as adjacency list
              : dict vertex_id => list of vertex_id's
        dist  : distance map
              : dict (begin_vertex,end_vertex) => distance
        returns: (minimum_cost, parent_map) where minimum cost is the cost of
                traversing the set, and parent map, maps vertex to a list
                of preciding vertecies'''
    class Path:
        ''' An internal class for representing paths which have already been
            explored.
            vertex_id is the end vertex, and is not in the visited_set, as per convention.
            vertex_id can not be in visited_set.
            all_verticies is the union of vertex_id and visited_set.'''
        def __init__(self, vertex_id, visited_set):
            self._vertex_id = copy.deepcopy(vertex_id)
            if visited_set is frozenset:
                self._visited_set = visited_set
            else:
                self._visited_set = frozenset(visited_set)
            self._all_verticies = None


        def __repr__(self):
            visited_labels = []
            for vertex in self.visited_set:
                visited_labels.append(vertex.__repr__())
            visited_set_str = "{" + ", ".join(visited_labels) + "}"
            return "(vertex_id={}, visited_set={})".format(self._vertex_id, self._visited_set)


        @property
        def vertex_id(self):
            ''' getter for _vertex_id '''
            return self._vertex_id


        @property
        def visited_set(self):
            ''' getter for _visited_set '''
            return self._visited_set


        @property
        def all_verticies(self):
            ''' getter for _all_verticies, calculated lazily '''
            if self._all_verticies is None:
                self._all_verticies = \
                    frozenset(self._visited_set.union([self._vertex_id]))
            return self._all_verticies


        def __hash__(self):
            return hash(self._vertex_id)*31 + hash(self._visited_set)


        def __eq__(self, rhs):
            return self._vertex_id == rhs.vertex_id and \
                self._visited_set == rhs.visited_set


        def  __ne__(self, rhs):
            return self._vertex_id != rhs.vertex_id or \
                self._visited_set != rhs.visited_set
        #end class Path

    # iterate through neighbors of vertex0, define path set, cost and parents
    # cost: 
    #  dict path => (minimal cost of traversing that path, parents_map)
    # where parents_map is a dict that maps vertex_id to a tuple of vertex id's
    if vertex0 is None:
        vertex0 = next(iter(graph))
    neighbors = graph[vertex0]
    cost = next_cost = {}
    parents = {}
    for vertex in neighbors:
        edge = (vertex0, vertex)
        if edge in dist:
            path = Path(vertex, frozenset())
            cost[path] = dist[edge]
            parents[vertex] = vertex0

    # iterate through succesively longer paths, until path of len(graph) is acheived
    # loop invariant: cost is the set of minimal distance paths beginning at vertex0 and 
    # ending at path.vertex. Each path is minimal in the sense that the parent pointers
    # backtrace to form a minimal length path
    for path_length in range(1, len(graph)):
        next_cost = {}
        if verbose:
            print( "path_length={}".format(path_length))

        #iterate through neighbors of previous path set to generate next path set
        for path, distance in cost.items():
            if verbose:
                print("path={} distance={}".format(path, distance))
            for neighbor in graph[path.vertex_id]:
                if verbose:
                    print("neighbor={}".format(neighbor))
                if not neighbor in path.visited_set:
                    edge = (path.vertex_id, neighbor)
                    # do not visit first vertex, until last iteration
                    if neighbor == vertex0 and path_length < len(graph)-1:
                        pass
                    if edge in dist:
                        test_cost = distance + dist[edge]
                        test_path = Path(neighbor, path.all_verticies)
                        if test_path in next_cost:
                            #this is the relaxation step
                            existing_cost = next_cost[test_path]
                            if test_cost < existing_cost:
                                next_cost[test_path] = test_cost
                                parents[neighbor] = [path.vertex_id]
                            elif test_cost == existing_cost:
                                parents[neighbor].append(path.vertex_id)
                        else:
                            next_cost[test_path] = test_cost
                            parents[neighbor] = [path.vertex_id]
        cost = next_cost
    #end while

    #final iteration, go through all paths of length N, find subset with minimal distance
    #define parent pointers to this subset
    min_cost = None
    cost = {}
    for path, path_cost in next_cost.items():
        if min_cost is None or path_cost < min_cost:
            min_cost = path_cost
            cost = {}
            cost[path] = path_cost
            parents[vertex0] = path.vertex_id
        elif cost == min_cost:
            cost[path] = path_cost
            parents[vertex0].append(path.vertex_id)

    return (cost, parents)
