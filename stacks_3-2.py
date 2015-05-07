# PROBLEM:

# How would you design a stack which, in addition to push and pop,
# also has a function min which returns the minimum element?
# Push, pop and min should all operate in O(1) time

# the challenge is the O(1) time.

# linked lists have O(1) insert, delete.

# min attribute is a bit more tricky.
# should have min() which is O(1), and suggests a primitive (int) attribute.
# but if remove current min, need history of previous min.
# use a min list, but are slicing to the list usually.

###########################################################


class Stack(object):

    def __init__(self):
        self.top_layer = None
        self.minimum = []

    def push(self, data):
        if len(self.minimum) == 0:
            self.minimum.append(data)
        elif self.minimum[-1] > data:
            self.minimum.append(data)
        self.top_layer = StackLayer(data, self.top_layer)

    def pop(self):
        value = self.top_layer.data
        self.top_layer = self.top_layer.previous
        if value == self.minimum[-1]:
            # determine new minimum
            self.minimum.pop(-1)
        return value

    def min(self):
        return self.minimum[-1]


class StackLayer(object):

    def __init__(self, data, previous):
        self.data = data
        self.previous = previous


test_stack = Stack()
test_stack.push(35)
test_stack.push(627)
test_stack.push(5)
test_stack.push(61)

# return 5
print test_stack.min()

# remove and return 61
print test_stack.pop()

# remove and return 5
print test_stack.pop()

# return 35
print test_stack.min()

