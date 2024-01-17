import PriorityQueueList

a = PriorityQueueList.PriorityQueueList()

a.enqueue(5)
a.dequeue()
print(a.is_empty())
print(a.size())
print(a)
a.enqueue(10)
a.enqueue(15)
a.enqueue(20)
a.enqueue(3)
print(a)
a.dequeue()
print(a)
a.enqueue(5)
print(a.size())
a.is_empty()
