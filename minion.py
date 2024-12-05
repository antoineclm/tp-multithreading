import queue_mc as q

taskQueue, resultQueue = q.connect_queue()
while True:
    t = taskQueue.get()
    result = t.work()
    print(result[0])
    resultQueue.put(result)
