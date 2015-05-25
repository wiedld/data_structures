# PROBLEM
#
# Write an algorithm to find the next node (in order successor)
# of a given node in a binary search tree
# where each node has a link to its parent.
#
#
# APPROACH
#     - traverse "in order" is left-parent-right
#     - node class with link to parent
#         - .next is the l-p-r traversal
#         - node with .left, .right, .parent
#     - .next, from the curr node
#         - looking for .next, not .previous, so don't go left (backwards)
#         - if have right child, go right, then as far left as possible
#         - if doesn't have right child, go to parent'
#             - if parent.left = current node, then parent is .next
#             - if parent.right - current node, then go all the way up to the super parent.right

################################################################

class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = None

        if self.left is not None:
            self.left.parent = self
        if self.right is not None:
            self.right.parent = self

    def next(self):
        if self.right is not None:
            # go to left most descendent of right child
            p = self.right
            while p.left is not None:
                p = p.left
            return p.data
        else:
            # if there is no right child, then go to super parent.
            p = self       # in case self is the root
            while p.parent is not None:
                p = p.parent
            return p.data



node_a = Node("A")
node_c = Node("C")
node_e = Node("E")
node_d = Node("D", node_c, node_e)
node_b = Node("B", node_a, node_d)

node_h = Node("H")
node_i = Node("I", node_h)
node_g = Node("G", None, node_i)

root_f = Node("F", node_b, node_g)

print node_e.parent.data       # D
print root_f.parent

print node_e.next()     # F
print root_f.next()     # G
