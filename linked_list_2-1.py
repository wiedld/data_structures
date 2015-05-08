# Write code to remove duplicates from an unsorted linked list.
#
# How would you solve this problem if a temporary buffer is not allowed? 


#############################################################
# SUBPROBLEMS:
# 1 - setup pointers
# 2 - visit all items in linked list, comparing to the value at compare
# 3 - move the compare pointer, and repeat #2.

#############################################################

def set_pointers(LL_node):
    previous = LL_node
    current = previous.next
    compare = LL_node

    return compare, previous, current


def compare_data(compare, previous, current):
    while current != None:
        print
        print "data for previous node:", previous.data
        print "current node object:", current

        if compare.data == current.data:
            current = current.next
            previous.next = current

        print "what current will be reassigned to:", current.next
        current = current.next
        previous = previous.next

    return

    
    # print
    # print "data for previous node:", previous.data
    # print "current node object:", current
    #
    # # base case
    # if current is None:
    #     print "hit line 29"
    #     return
    #
    # print "hit line 33"
    # # changing linked list
    # if compare.data == current.data:
    #     current = current.next
    #     previous.next = current
    #
    # # move pointers forward
    # print "line 39, current.next:", current.next
    # current = current.next
    # print "line 41, current obj:", current
    # previous = previous.next
    #
    # # recursive call
    # return compare_data(compare, previous, current)


def remove_duplicates(comparison_node):
    # make pointers
    compare, previous, current = set_pointers(comparison_node)
    # find and remove duplicates of the comparison_node
    compare_data(compare, previous, current)
    # change the state = move the comparison_node
    comparison_node = comparison_node.next
    # recursive call
    return remove_duplicates(comparison_node)


class LL_node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


nodeF = LL_node(2)
nodeE = LL_node(0, nodeF)
nodeD = LL_node(3, nodeE)
nodeC = LL_node(4, nodeD)
nodeB = LL_node(2, nodeC)
nodeA = LL_node(3, nodeB)

remove_duplicates(nodeA)


