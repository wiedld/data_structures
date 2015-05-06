# PROBLEM

# Implement a function to check if a tree is balanced
# For the purposes of this question, a balanced tree is defined to be a tree such that no two leaf nodes differ in distance from the root by more than one

################################################################

# approach:
# - levels = depth.  DFS.
# - when hit curr_node = none, you have hit the leaf. define min & max
# - each time hit a leaf, compare and update min/max
# - state variable is needed to track levels.


def is_bt_balanced(node):
    # get levels
    min_l, max_l = get_levels(node)

    if (max_l-min_l) > 1:
        return False
    return True


def get_levels(curr_node, level=1, min_l=None, max_l=1):
    # base case
    if curr_node is None:
        # define variables the first time
        if min_l is None:
            min_l = level
        min_l = min(min_l, level)
        max_l = max(max_l, level)

        return min_l, max_l

    # update level for next recursive call
    level += 1

    min_1, max_1 = get_levels(curr_node.left, level, min_l, max_l)
    min_2, max_2 = get_levels(curr_node.right, level, min_l, max_l)

    return min(min_1, min_2), max(max_1, max_2)


# TEST
class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# make a balanced tree
L3_1 = Node("L3_1")
L3_2 = Node("L3_2")
L2_1 = Node("L2_1", L3_1, L3_2)
L2_2 = Node("L2_2")
L1_1 = Node("L1_1", L2_1, L2_2)

print is_bt_balanced(L1_1)

# make unbalanced tree
B4_1 = Node("B4_1")
B3_1 = Node("B3_1", B4_1)
B3_2 = Node("B3_2")
B2_1 = Node("B2_1", B3_1, B3_2)
B2_2 = Node("B2_2")
B1_1 = Node("B1_1", B2_1, B2_2)

print is_bt_balanced(B1_1)

