# PROBLEM:  reverse a singly linked list

# Need to have:
    # - start with A > B > C > D
    # - build the kernal.  move D to front.
    #     D > A > B > C

    # - have D  be p_insert_start
    # - have A  be p_insert_end
    # - p_to_move will now be C.  To be inserted between D and A.
    #     D > C > A > B
    # - p_start moves fwd once (to C)

    # - now have C  as p_insert_start
    # - have A  as p_insert_end
    # - p will be moved to the end.

    # repeat
    # base case: p_insert_end (node A) has .next == None



#####################################################

def reverse_LL(head):
    # make the new head.  Save the new head (to be returned at the end)
    new_head = detach_and_return_tail(head)
    new_head.next = head

    # p_insert_start is the new head, node D.
    # things will be inserted btwn D and A.
    p_insert_start = new_head
    p_insert_end = head

    reverse_LL_3p(p_insert_start, p_insert_end)

    # return new head
    return new_head



def detach_and_return_tail(pointer):
    """get to the second to last node.  Disconnect and return the last node."""
    while pointer.next.next != None:
        pointer = pointer.next

    # disconnect current tail and return.  make new tail.
    disconnected_tail = pointer.next
    pointer.next = None
    return disconnected_tail



def reverse_LL_3p(p_insert_start, p_insert_end):
    # base case.  stop when node A (p_insert_end) is at the end.
    if p_insert_end.next == None:
        return
    # make pointer, and get the current tail
    p_to_move = detach_and_return_tail(p_insert_end)
    # insert between two pointers
    p_insert_start.next = p_to_move
    p_to_move.next = p_insert_end
    # inch the first pointer forward
    p_insert_start = p_insert_start.next

    reverse_LL_3p(p_insert_start, p_insert_end)



def print_node_order(curr):
    if curr == None:
        return
    print curr.data
    print_node_order(curr.next)



class LL_node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


E = LL_node("E")
D = LL_node("D",E)
C = LL_node("C",D)
B = LL_node("B",C)
A = LL_node("A",B)


new_head = reverse_LL(A)
print_node_order(new_head)

