# PROBLEM: Describe how you could use a single array to implement three stacks

# PROPOSED SOLUTION:
# - treat a single array like memory slots.
# - Then each stack is similar to a linked list.
#     - one mem slot (array position) is the data.
#     - adjacent mem slot (array position) is the pointer to the previous item
#     - to create the Filo aspect of a stack:
#         - the pointer goes from the next added value, to the previous value using a singly linked .lower (e.g. .next).
#         new_value.lower = previous_value

###############################################################

# As a learning experience, will try to make one.
# as I believe this is how linked lists work with memory slots.


# mem_array = []

class Stack(object):
    # global mem_array
    mem_array = []

    def __init__(self):
        pointer = ""
        # stack ends with a pointer to none at idx = last_added.
        self.mem_array.extend(["None", pointer])
        # update last added for new value
        self.last_added_idx = len(self.mem_array)-2

    def add(self, data):
        # points to previously added
        pointer = self.last_added_idx
        self.mem_array.extend([data, pointer])
        # update last added for new value
        self.last_added_idx = len(self.mem_array)-2



# create a stack.
test_stack = Stack()
test_stack.add("first_1")
test_stack.add("second_1")
print test_stack.mem_array

# create another stack, and should build into single array
test_stack_2 = Stack()
test_stack_2.add("first_2")
test_stack_2.add("second_2")
print test_stack_2.mem_array

# what if I add to the original stack.
# Does it correctly update the pointer in the array?
test_stack.add("third_1")
test_stack_2.add("third_2")
print test_stack.mem_array






