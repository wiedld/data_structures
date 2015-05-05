"""for a given bst, write a function that prints out the nodes in order of increasing data value"""

# APPROACH:

# go as far left as possible, print .data
# return up to parent and print .data
# then go right the print .data

# recursively continue
# base case: when curr_node == None

# state = keep track of visited, so do not double print when going up the stack frame.

##############################################################

class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right



left_subtree = Node(5, Node(3, Node(1, Node(0), Node(2))), Node(8) )
right_subtree = Node(34, Node(21), Node(55, None, Node(144, Node(89), Node(233) )) )

root_tree = Node(13,left_subtree, right_subtree)




def print_bst_data_in_order(curr_node, visited=[]):
    # base case
    if curr_node.left==None and curr_node.right==None:
        return curr_node

    # print left first
    if curr_node.left != None and curr_node.left not in visited:
        node = print_bst_data_in_order(curr_node.left, visited)

        if node not in visited:
            print node.data
            visited.append(node)

    # print current node
    if curr_node.data not in visited:
        print curr_node.data
        visited.append(curr_node)

    # print right node
    if curr_node.right != None and curr_node.right not in visited:
        node = print_bst_data_in_order(curr_node.right, visited)

        if node not in visited:
            print node.data
            visited.append(node)

    return curr_node



print_bst_data_in_order(root_tree)


