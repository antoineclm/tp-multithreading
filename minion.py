import queue_mc as q


qc = q.QueueClient()
while True:
    t = qc.taskQueue.get()
    result = t.work()
    print(result[0])
    qc.resultQueue.put(result)
