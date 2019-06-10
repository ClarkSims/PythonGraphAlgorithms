#!/usr/bin/env python3
''' can be imported or run alone as demo
    ./print_binary_tree.py  > demo.gv
    dot -Tpng -o demo.png demo.gv
    '''

class Node:
    ''' basic node '''
    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val


def partially_complete_binary_tree_from_list(lst, off=0):
    if not lst:
        return None
    nd = Node(lst[off])
    #explore left child
    chld = 2*off + 1
    if chld < len(lst) and lst[chld] is not None:
        nd.left = partially_complete_binary_tree_from_list(lst, chld)
    #explore right child
    chld += 1
    if chld < len(lst) and lst[chld] is not None:
        nd.right = partially_complete_binary_tree_from_list(lst, chld)
    return nd


def write_tree_to_dot(root, out, options=[]):
    out.write("digraph G {\n")
    for opt in options:
        out.write("    {}".format(opt))
    write_node(root, out)
    out.write("}\n")


def write_gsv_file(root, filename):
    with open(filename, "w") as out:
        write_tree_to_dot(root, out)


def write_node(node, out, parent_id = None, prev_id = None):
    if prev_id is not None and parent_id is not None:
        id = prev_id + 1
        out.write("    {} -> {}\n".format(parent_id, id))
    else:
        id = 0
    out.write("    {} [label=\"{}\"]\n".format(id, node.val))
    prev_id = id
    if node.left is not None:
        prev_id = write_node( node.left, out, id, prev_id)
    if node.right is not None:
        prev_id = write_node( node.right, out, id, prev_id)
    return prev_id


if __name__=='__main__':
    import sys
    vals = [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14]
    root = partially_complete_binary_tree_from_list(vals)
    write_tree_to_dot(root, sys.stdout)
