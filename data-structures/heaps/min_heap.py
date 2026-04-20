class Heap:
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
        idx = 1
        while True:
            
            left = 2 * idx + 1
            right = 2 * idx + 2
            min = idx

            if left < len(self.heap) and self.heap[left] < self.heap[min]:
                min = left
            if right<len(self.heap) and self.heap[right] < self.heap[min]:
                min = right
            
            # exit if parent is min
            if min == idx:
                break
            
            # swap min child with parent
            self.heap[idx], self.heap[min] = self.heap[min], self.heap[idx]
            idx = min
        
        # return the min value
        return res
