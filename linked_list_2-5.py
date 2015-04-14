# PROBLEM
# You have two numbers represented by a linked list, where each node contains a sin- gle digit The digits are stored in reverse order, such that the 1’s digit is at the head of the list Write a function that adds the two numbers and returns the sum as a linked list
# EXAMPLE
# Input: (3 -> 1 -> 5) + (5 -> 9 -> 2)
# Output: 8 -> 0 -> 8

# bigO, time.  O(n) where n = length of longest input LL.
# bigO, space. n or n+1, based on if there is carryover on the last addition.


def LL_sum(LL1, LL2):
    LL1_N = LL1.head
    LL2_N = LL2.head
    LL3 = LL()
    LL3_N = LL3.head

    while True:
        if LL1_N==None and LL2==None:
            return LL3
            # note this LL3 has a final node which could be empty if no value is carried.

        summed = node_data(LL1_N) + node_data(LL2_N)
        # add to carried value in data
        LL3_N.data = summed%10 + LL3_N.data

        LL1_N, LL2_N = node_next(LL1_N), node_next(LL2_N)
        # make the next node, with the carried value
        LL3_N = output_LL_next(LL3_N, summed/10)



def node_data(N):
    if N==None:
        return 0
    else:
        return N.data

def node_next(N):
    if N==None:
        return None
    else:
        return N.next

def output_LL_next(N, data):
    N.next = LL_N(data)
    return N.next

class LL_N(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LL(object):
    def __init__(self, head=LL_N(),tail=LL_N()):
        self.head = head
        self.tail = tail

