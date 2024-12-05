import queue_mc as q
from task import Task

qc = q.QueueClient()
t1 = Task(1, 10)
t2 = Task(2, 10)
t3 = Task(3, 10)
t4 = Task(4, 10)
qc.taskQueue.put(t1)
qc.taskQueue.put(t2)
qc.taskQueue.put(t3)
qc.taskQueue.put(t4)

t = Task()
while 1:
    t = qc.resultQueue.get()
    print(t)
