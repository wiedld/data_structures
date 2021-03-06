# Write code to remove duplicates from an unsorted linked list.
#
# How would you solve this problem if a temporary buffer is not allowed? 


#############################################################
# SUBPROBLEMS:
# 1 - setup pointers
# 2 - visit all items in linked list, comparing to the value at compare
# 3 - move the compare pointer, and repeat #2.

#############################################################

def set_pointers(ll_node):
    previous = ll_node
    current = previous.next
    compare = ll_node

    return compare, previous, current


def compare_data(compare, previous, current):
    while current is not None:

        if compare.data == current.data:
            current = current.next
            previous.next = current

            if current is None:
                break

        current = current.next
        previous = previous.next

    return


def remove_duplicates(comparison_node):
    # base case = comparison_node is the last node
    if comparison_node.next is None:
        return
    # make pointers
    compare, previous, current = set_pointers(comparison_node)
    # find and remove duplicates of the comparison_node
    compare_data(compare, previous, current)
    # change the state = move the comparison_node
    comparison_node = comparison_node.next
    # recursive call
    return remove_duplicates(comparison_node)


class LLnode(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def print_ll(self):
        print self.data
        next_node = self.next
        if next_node is None:
            return
        next_node.print_ll()


nodeF = LLnode(2)
nodeE = LLnode(0, nodeF)
nodeD = LLnode(3, nodeE)
nodeC = LLnode(4, nodeD)
nodeB = LLnode(2, nodeC)
nodeA = LLnode(3, nodeB)

nodeA.print_ll()
print
remove_duplicates(nodeA)
nodeA.print_ll()


