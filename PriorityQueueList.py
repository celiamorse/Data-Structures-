#this is a very basic list-based queue to get you started on the C-level project

class PriorityQueueList:
    
    def __init__(self):
        self.items = []
        
    
    def enqueue(self, i): 
        # start at beginning of list 
        work = 0 
        index = len(self.items)-1
        # iterate through the list until you get to the end, or the item you are inserting is less than the item at the current index 
        while index >=0 and i >= self.items[index]:
            work += 1 # increment for each iteration
            index -= 1 
        
        # insert item at the index where the while loop fails to be true 
        self.items.insert(index + 1, i)  
        work += 1 # increment for insertion
   
        return work 
    def dequeue(self): 
        work = 0
        
        if self.is_empty(): # checks if the queue is empty. if it is, return None.
            return None 
        
        item = self.items.pop(0)
        work += 1 # removal 
        work += len(self.items)# increment by 1 for pop
       
        return item and work# if the queue is not empty, remove and return the item at index 0. 
        
    
    def size(self):
     
        return len(self.items) # return length of the list 

    def is_empty(self):
     
        return self.items == [] # checks if the queue is empty. returns a boolean
    
    def __str__(self):

        return str(self.items) # returns self.items as a strand
   