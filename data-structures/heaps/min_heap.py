class MinHeap:
    def __init__(self):
        self.heap = [0]

    # O(log N)
    # adds new value to the end of the tree 
    # & reorders values so that in each subtree parent is minimum
    def push(self, val):
        # 1. append new value to the end of arraylist
        self.heap.append(val)

        # get the index of added value
        i = len(self.heap) - 1

        # 2. percolate up:
        # compare new value to its parent
        # swap new value if it is less than parent value
        # keep repeating until new value is less than parent value
        while self.heap[i] < self.heap[i // 2]:
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i = i // 2

    # O(log N)
    # returns the min value from the root of the tree
    def pop(self):
        # 1. return quickly if arraylist empty
        # the value in index 0 is placeholder
        if len(self.heap) == 1:
            return None
        
        # remove and return if only root value available
        if len(self.heap) == 2:
            return self.heap.pop()

        # otherwise, get the min value from the root as a return value
        res = self.heap[1]

        # move the last item to root 
        self.heap[1] = self.heap.pop()
        
        # percolate down
        i = 1
        while True:
            left = 2 * i
            right = 2 * i + 1

            min = i
            
            if left < len(self.heap) and self.heap[left] < self.heap[i]:
                min = left
            if right < len(self.heap) and self.heap[right] < self.heap[i]:
                min = right
            
            if min == i:
                break
            
            self.heap[min], self.heap[i] = self.heap[i], self.heap[min]
            i = min
            
        
        # return the min value
        return res

    def __str__(self):
        return f"{self.heap}"
    
h = MinHeap()
h.push(3)
h.push(2)
h.push(6)
h.push(4)
h.push(1)
print(h)        # [0, 1, 2, 6, 4, 3]

print(h.pop())  # 1
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