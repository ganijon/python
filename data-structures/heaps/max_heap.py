class MaxHeap:
    """
    Max-heap stores values in arraylist and returns the max value in O(1).
    Push and Pop is completed in O(logN) time.

    All values in arraylist structured as a complete binary tree where:
    - each parent value is greater than its children's values
    - each level is full, but the leaf-level filled from left to right
    - position of a left child of a parent at index i:  left=2*i
    - position of a right child of a parent at index i: right=2*i+1
    - position of a parent of a child node at index i:  parent=i//2

    In this implementation, the value in 0-index is unused, but reserved as
    a placeholder to simplify the calculations.
    """

    def __init__(self):
        self.heap = [0]

    def push(self, val):
        """
        Appends val to the end of the heap and
        percolates it up the tree recursively
        until it greater than its parents
        """
        self.heap.append(val)
        i = len(self.heap) - 1
        while i // 2 > 0:
            if self.heap[i] > self.heap[i // 2]:
                self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i = i // 2
        return val

    def pop(self):
        """
        Removes and returns the max value from the top of the heap,
        moves the last item to the top and percolates it down the
        tree recursively until it is less than its children
        """
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()
        
        res = self.heap[1]
        self.heap[1] = self.heap.pop()

        i = 1
        while True:
            left = 2 * i
            right = 2 * i + 1
            max = i
            
            # [0, 1, 4, 3, 2]
            
            if left < len(self.heap) and self.heap[left] > self.heap[i]:
                max = left
            if right < len(self.heap) and self.heap[right] > self.heap[left] and self.heap[right] > self.heap[i]:
                max = right
            
            if max == i:
                break
            
            self.heap[i], self.heap[max] = self.heap[max], self.heap[i]
            i = max

        return res

    def __str__(self):
        return f"{self.heap}"


h = MaxHeap()
h.push(3)
h.push(2)
h.push(6)
h.push(4)
h.push(1)
print(h)  # [0, 6, 4, 3, 2, 1]

print(h.pop())  # 6
print(h)        # [0, 2, 3, 6, 4]

print(h.pop())  # 2
print(h)        #[0, 3, 4, 6]

print(h.pop())  # 3
print(h)        # [0, 4, 6]

print(h.pop())  # 4
print(h)        # [0, 6]

print(h.pop())  # 6
print(h)        # [0]

print(h.pop())  # None
print(h)        # [0]
