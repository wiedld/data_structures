# PROBLEM

# Given a binary search tree, design an algorithm which creates a linked list
# of all the nodes at each depth

######################################################
# APPROACH:
#
# - breadth first
# - base case: no children and queue is empty
# - update states:
#     - children into back of queue
#     - make a new LL of all children

# - pass front of queue to the next recursive call
#
######################################################

class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class LLnode(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def print_nodes(self):
        current = self
        if current.next is None:
            print current.data
            return
        print current.data
        current.next.print_nodes()


nodeC4 = Node("C4")
nodeC3 = Node("C3")
# nodeC2 = Node("C2")
nodeC1 = Node("C1")
nodeB2 = Node("B2", nodeC3, nodeC4)
nodeB1 = Node("B1", nodeC1)
nodeA = Node("A", nodeB1, nodeB2)


import Queue

def bt_into_ll_per_level(node):
    q = Queue.Queue()
    q.put(node)
    ll_node = LLnode()
    result = []
    result.append(ll_node)

    while not q.empty():
        curr_node = q.get()
        # print "current:", curr_node.data

        ll_node.next = LLnode(curr_node.data)
        ll_node = ll_node.next

        if curr_node.left is not None:
            q.put(curr_node.left)
        if curr_node.right is not None:
            q.put(curr_node.right)

    return result


print bt_into_ll_per_level(nodeA)[0].print_nodes()
