import queue_mc as q
from task import Task

taskQueue, resultQueue = q.connect_queue()
t1 = Task(identifier=1)
t2 = Task(identifier=2)
t3 = Task(identifier=3)
t4 = Task(identifier=4)
taskQueue.put(t1)
taskQueue.put(t2)
taskQueue.put(t3)
taskQueue.put(t4)


result = [0, 0, 0]

while result[0] != 4:
    result = resultQueue.get()
    print(result[0])
