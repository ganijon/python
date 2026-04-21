class MaxHeap:
    '''
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
    '''
    
    
    def __init__(self):
        self.heap = [0]
    
    def push(self, val):
        ''' 
        Appends val to the end of the heap and
        percolates it up the tree recursively
        until it greater than its parents
        '''
        
        return val
    
    def pop(self):
        '''
        Removes and returns the max value from the top of the heap, 
        moves the last item to the top and percolates it
        down the tree recursively until it is less than its children
        '''
        
        return self.heap[0]
    
    def __str__(self):
        return f"{self.heap}"