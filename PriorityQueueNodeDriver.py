import PriorityQueueNode


queue = PriorityQueueNode.PriorityQueueNode()


queue.enqueue(1)
print(queue.size())
print(queue.is_empty())
queue.dequeue()
print(queue.is_empty())

pq = PriorityQueueNode.PriorityQueueNode()
pq.enqueue(1)
pq.enqueue(2)
pq.enqueue(3)
pq.enqueue(4)
pq.enqueue(5)
print(pq.size())
print(pq.dequeue())
print(pq.size())
print(pq.is_empty())



