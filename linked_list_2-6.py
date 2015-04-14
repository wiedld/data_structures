# PROBLEM
# Given a circular linked list, implement an algorithm which returns node at the begin- ning of the loop

# DEFINITION
# Circular linked list: A (corrupt) linked list in which a node’s next pointer points to an earlier node, so as to make a loop in the linked list
# EXAMPLE
# input: A -> B -> C -> D -> E -> C [the same C as earlier]
# output: C

########################################
# ANSWER:  if given linked list made with these classes:

class LL_N(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LL(object):
    def __init__(self, head=LL_N(),tail=LL_N()):
        self.head = head
        self.tail = tail

    def add(self, node):
        self.tail.next=node
        self.tail=node


A, B, C, D, E = LL_N("A"), LL_N("B"), LL_N("C"), LL_N("D"), LL_N("E")
linked_list = LL(A)
linked_list.add(B)          # add method makes A point to B
linked_list.add(C)
linked_list.add(D)
linked_list.add(E)          # E still points to none
E.next = C                  # but E should still be the tail


def find_loop_crossing(LL):
    return LL.tail.next     # returns C

