# PROBLEM
# Write code to partition a linked list around a value x, such that all modes less than x come before all nodes greater than or equal to x.


#######################################################
# using three new linked lists, with concat at the end.
# assume all are singly linked lists
# bigO, time. single while loop, and 2 concats. O(n) +2
# bigO, space. 3 additional lists, but total is the original N size.

def sort_around_pivot(x, start_LL):
    smaller_LL = LL()
    equal_LL = LL()
    larger_LL = LL()
    curr = start_LL.head

    while curr != None:
        pointer = curr.next # save point, since add method will remove ".next"
        if curr.data < x:
            smaller_LL.add(curr)
        elif curr.data < x:
            larger_LL.add(curr)
        else:
            equal_LL.add(curr)
        curr = pointer

    return concat(smaller_LL, concat(equal_LL,larger_LL) )




class LL_N(object):
    def __init__(self, data=None):
        self.data = data


class LL(object):
    def __init__(self, head=LL_N(),tail=LL_N()):
        self.head = head
        self.tail = tail

    def add(self,node):
        self.tail.next = node
        self.tail = node
        self.tail.next = None


def concat(LL1, LL2):
    LL1.tail.next = LL2.head
    LL1.tail = LL2.tail
    return LL1



#######################################################
# perform in place.
# assume is a doubly linked list.
# bigO, time. single while loop, linking is k contant events. O(n) + k.
# bigO, space. constant plus curr/p1/p2.  +3 constant spaces

def in_place_sort_pivot(DLL, x):
    p1, p2, curr = None, None, DLL.head

    #first time through.  p1/p2 stays on head as curr.data > x.

    while curr != None:
        if curr.data > x:
            curr = curr.next
        elif curr.data < x:
            move_before_p1(curr, p1, DLL)
        else:
        # if data = x.  should be btwn p1 and p2.
            move_before_p2(curr, p2, DLL, p1)

    return DLL




def move_before_p1(node, p1, DLL):
    # before moving node, connect previous to next.  Looping out node
    node.previous.next = node.next
    node.next.previous = node.previous

    if p1 == None:
        assign_p1(node, DLL)
    else:
        # insert into DLL at before p1
        p1.previous.next = node
        node.next = p1
        p1.previous = node



def move_before_p2(node, p2, DLL, p1):
    # before moving node, connect previous to next.  Looping out node
    node.previous.next = node.next
    node.next.previous = node.previous

    if p2 == None:
        assign_p2(node, DLL, p1)
    else:
        # insert into DLL at before p2
        p2.previous.next = node
        node.next = p2
        p2.previous = node




def assign_p1(node, DLL):
    p1 = node

    if DLL.head != p1:
    # if node is not the head, then make the head
        DLL.head.previous = p1
        p1.next = DLL.head
        DLL.head = p1



def assign_p2(node, DLL, p1):
    p2 = node

    if p1 == None:
    # if p1 is None, make p2 the head.
    # then once p1 is made, it will become the head in front
        DLL.head.previous = p2
        p2.next = DLL.head
        DLL.head = p2
    else:
    # if p1 exists already, place p2 right after
        p1.next.previous = p2
        p2.next = p1.next
        p1.next = p2




class DLL_N(object):
    def __init__(self, data=None, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous


class DLL(object):
    def __init__(self, head=LL_N(),tail=LL_N()):
        self.head = head
        self.tail = tail

