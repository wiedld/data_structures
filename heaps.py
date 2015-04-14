
class Heaps(object):
    """data is an array indexed 0 to n-1.  But position is a number from 1 to n.  Using position allows for int math to find the parent."""

    def __init__(self, data=[]):
        self.data = data

    def insert(self, value):
        self.data.append(value)
        print self.data
        position = len(self.data)
        self.bubble_up(position)

    def bubble_up(self, position):
        parent = position/2
        # base cases.
        if position == 1:
            return
        if self.data[position-1] > self.data[parent-1]:
            return
        # swap & recursive call
        self.data[position-1], self.data[parent-1] = self.data[parent-1], self.data[position-1]
        print self.data
        # recursive call
        self.bubble_up(parent)



    def extract_min(self):
        extracted_min = self.data[0]
        self.data[0] = self.data[-1]
        self.data.pop(-1)
        self.bubble_down(1)
        return extracted_min



    def bubble_down(self, parent):
        print self.data

        l_child, r_child = (parent*2), ((parent*2)+1)

        # base case.  No more children
        if len(self.data) <= l_child:
            return

        # right is smaller then left
        if self.data[r_child-1]!=None and self.data[r_child-1]<=self.data[l_child-1]:
            # compare to parent.
            if self.data[r_child-1]>=self.data[parent-1]:
                return
            # swap & recursive call
            self.data[parent-1], self.data[r_child-1] = self.data[r_child-1], self.data[parent-1]
            self.bubble_down(r_child)

        # left is smaller than right (or there is no right child)
        # compare to parent
        if self.data[l_child-1]>=self.data[parent-1]:
                return
        # swap & recursive call
        self.data[parent-1], self.data[l_child-1] = self.data[l_child-1], self.data[parent-1]
        self.bubble_down(l_child)




alist = [4,4,8,7,9]
aheap = Heaps(alist)

# test insert
aheap.insert(2)
aheap.insert(8)
aheap.insert(6)
aheap.insert(12)

# test extract min
heap_min = aheap.extract_min()
print "heap min:", heap_min
