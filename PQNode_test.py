import random
import PriorityQueueNode

random.seed(2007)

# re-initialize the data collection file
file = open("PriorityQueueNode.csv","w")
file.write("operation, n, work\n")
file.close()

# run experiments on priority queue
file_pq = open("PriorityQueueNode.csv","a") #open in append mode so the data isn't overwritten

# create a queue with a fixed size
pq = PriorityQueueNode.PriorityQueueNode()
for j in range(1000):
    # fill the queue with random integers
    pq.enqueue(random.randint(11,100000))

for i in range(20): #we're going to run 20 experiments
    # set up the tests and check how long it takes to insert a new item of high priority
    high_priority_item = random.randint(100001, 1000000)
    work = pq.enqueue(high_priority_item) 

    file_pq.write("Enqueue, "+str(pq.size())+", "+str(work)+"\n")
    print(f"Inserted {high_priority_item} into a queue with size {pq.size()}")

    work1 = pq.dequeue()

    file_pq.write("Dequeue, "+str(pq.size())+", "+str(work)+"\n")
    


print("End priority queue insert\n")
file_pq.close()

print("Done. Check the files for your test results")
