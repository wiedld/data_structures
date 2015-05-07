
class Node(object):
    def __init__(self, data=None, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous

    def set_previous(self, previous=None):
        self.previous = previous
        # base case
        if self.next is None:
            return
        # update state
        prev_pointer = self
        next_node = self.next
        # recursive call
        next_node.set_previous(prev_pointer)

    def print_nodes_fwd(self):
        curr_node = self
        while curr_node is not None:
            print curr_node.data
            curr_node = curr_node.next

    def print_nodes_rev(self):
        curr_node = self
        while curr_node is not None:
            print curr_node.data
            curr_node = curr_node.previous


node4 = Node(4)
node3 = Node(3, node4)
node2 = Node(2, node3)
node1 = Node(1, node2)

# set previous call
node1.set_previous()

# test success
node4.print_nodes_rev()
print
node1.print_nodes_fwd()

