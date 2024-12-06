import queue_mc as q
from task import Task

qc = q.QueueClient()

result = Task()
while True:
    t = qc.taskQueue.get()
    t.work()
    print("tache : " + str(t.identifier) + " en : " + str(t.time))
    qc.resultQueue.put(t)
