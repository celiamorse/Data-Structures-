import Node 
class PriorityQueueNode:
    
    def __init__(self):
        self._front = None
        self._rear  = None 
        self._length = 0 
        
    def enqueue(self, item):
    # add to the back of the queue. Rear points to None
        new_node = Node.Node(item)
        work = 0 
        if self.is_empty(): # if queue is empty, the new node becomes the front and the rear
            self._front = new_node
            self._rear = new_node
            work += 2 # updating the front and the rear of the queue
            
   
        else: # if the queue is not empty, traverse the list starting from the front until it finds appropriate position
            current_node = self._front
            prev_node = None
            while current_node is not None and item >= current_node.get_data() :
                prev_node = current_node
                current_node = current_node.get_next()
                work += 2 # two comparisons for each loop 
        # insert node in appropriate position
            if prev_node is None:  # adding node to front
                new_node.set_next(self._front)
                self._front = new_node
                work += 1 # setting new front node 
            elif current_node is None:  # adding node to the rear
                self._rear.set_next(new_node)
                self._rear = new_node
                work += 1 # setting new rear node 
            else:  # add node to the middle
                prev_node.set_next(new_node)
                new_node.set_next(current_node)
                work += 2 # two assignments. inserting new node and updating next node

        self._length += 1 # length is incremented by 1
        work += 1
        return work
            
    
        
            
    def dequeue(self): 
        work = 0
        if self.is_empty(): # if the queue is empty, return None
            return None
      
        item = self._front.get_data() # temporary data = the data within the front node in queue
        self._front = self._front.get_next() # front now set to the next node in the queue
        self._length -= 1 # length of queue minus 1 whenever dequeue is implemented
        work += 3 #  update front node , getting front, and decreasing length
        if self.is_empty(): # if the queue is empty, rear will also = None
            self._rear = None
            work += 1 # update rear node 
        work += self._length # shift all items down
        return item # return temporary data
        
            
    def __str__(self):
        s = "" # empty stirng is created
        next = self._front # temp variable is set to point at the front 
        while next != None: # while next is not none, data is added to string along with a space, then returned
            s += str(next.get_data()) + " " 
            next = next.get_next()
        return s

    def is_empty(self): 
        if self._front == None: #  if the queue is empty
            return True # return true. Otherwise, return false
        return False 
    def size(self):
        return self._length # size of queue is returned

    

