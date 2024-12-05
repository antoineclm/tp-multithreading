from multiprocessing.managers import BaseManager
from multiprocessing import Queue


class QueueManager(BaseManager):
    pass


class QueueClient:
    def __init__(self):
        QueueManager.register("get_taskQueue")
        QueueManager.register("get_resultQueue")
        m = QueueManager(address=("", 2430), authkey=b"bonjour")
        m.connect()
        self.taskQueue = m.get_taskQueue()
        self.resultQueue = m.get_resultQueue()


if __name__ == "__main__":
    taskQueue = Queue()
    resultQueue = Queue()
    QueueManager.register("get_taskQueue", callable=lambda: taskQueue)
    QueueManager.register("get_resultQueue", callable=lambda: resultQueue)
    m = QueueManager(address=("", 2430), authkey=b"bonjour")
    s = m.get_server()
    s.serve_forever()
