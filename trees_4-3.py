# PROBLEM

# Given a sorted (increasing order) array, write an algorithm to create a binary tree with minimal height

# ################################################

# approach:

# I'm assuming they want a search tree, which is why the array is ordered.

# - minimal height = balanced.  start at midpoint in array
# - split in three parts.
#     midpt = curr.data.
#     make left child, and right child
#     pass [:midpt] and left child to recursive call
#     pass [midpt:] and right child to recursive call

# base case = nothing left in the array
# state = array passed


class Node(object):
    def __init__(self, parent=None, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def print_node(self):
        if self.parent is not None:
            return "data: %s, parent.data: %s" % (str(self.data), str(self.parent.data))
        return "data: %s, parent in None" % (str(self.data))


def build_bst(array_x, curr_node=Node()):
    # base case.  midpt math works with len(1), midpt = [0] index
    if len(array_x) == 0:
        return

    midpt = len(array_x)/2
    curr_node.data = array_x[midpt]

    print curr_node.data
    print curr_node.print_node()

    left_array, right_array = array_x[:midpt], array_x[(midpt+1):]

    if len(left_array) > 0:
        curr_node.left = Node(curr_node)
        build_bst(left_array, curr_node.left)
    if len(right_array) > 0:
        curr_node.right = Node(curr_node)
        build_bst(right_array, curr_node.right)

test = [1, 2, 3, 4, 5, 6, 7]
build_bst(test)








