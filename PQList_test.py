import random
import PriorityQueueList

random.seed(2007)

# re-initialize the data collection file
file = open("PriorityQueueList.csv","w")
file.write("operation, n, work\n")
file.close()

# run experiments on priority queue
file_pq = open("PriorityQueueList.csv","a") #open in append mode so the data isn't overwritten

# create a queue with a fixed size
pq = PriorityQueueList.PriorityQueueList()
for j in range(1000):
    # fill the queue with random integers
    pq.enqueue(random.randint(11,100000))

for i in range(20): #we're going to run 20 experiments
    # set up the tests and check how long it takes to insert a new item of high priority
    item  = random.randint(100001, 1000000)
    work = pq.enqueue(item)

    file_pq.write("Enqueue, "+str(pq.size())+", "+str(work)+"\n")
    print(f"Inserted {item} into a queue with size {pq.size()}")

    work1 = pq.dequeue()
    file_pq.write("Dequeue, "+str(pq.size())+", "+str(work1)+"\n")
    



print("End priority queue insert\n")
file_pq.close()

print("Done. Check the files for your test results")
