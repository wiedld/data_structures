# PROBLEM

# Implement a function to check if a linked list is a palindrome.

#############################################################
# assume a doubly linked list
# given head node, no class for DLL
# return boolean
# bigO, time. 2n where n = length DLL.
# bigO, space. constant

def ck_DLL_is_palindrome(head):
    # make two pointers
    p1 = head
    p2 = head
    # move p2 to the back, return length value
    length = p_traverse(p2)
    return ck_palindrome(p1,p2, length/2)



class DLL_N(object):
    def __init__(self, data=None, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous


def p_traverse(p):
    length = 1
    while p.next != None:
        length +=1
        p = p.next
    return length


def ck_palindrome(p_front,p_back, steps):
    while steps > 0:
        if p_front.data != p_back.data:
            # early exit
            return False
        steps = steps -1
        p_front, p_back = p_front.next, p_back.previous

    return True


#############################################################
# assume a singly linked list
# given head node
# return boolean
# bigO, time. n where n = length LL.
# bigO, space. 2 strings made, constants

def ck_LL_is_palindrome(head):
    curr = head
    tracker = ""
    tracker_reversed=""
    while curr != None:
        tracker = tracker + str(curr.data)
        tracker_reversed = tracker_reversed + str(curr.data)
        curr = curr.next
    return tracker == tracker_reversed



class LL_N(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


