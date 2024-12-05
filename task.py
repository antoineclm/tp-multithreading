import time
import json
import numpy as np


class Task:
    def __init__(self, identifier=0, size=None):
        self.identifier = identifier
        # choosee the size of the problem
        self.size = size or np.random.randint(300, 3_000)
        # Generate the input of the problem
        self.a = np.random.rand(self.size, self.size)
        self.b = np.random.rand(self.size)
        # prepare room for the results
        self.x = np.zeros((self.size))
        self.time = 0

    def work(self):
        start = time.perf_counter()
        self.x = np.linalg.solve(self.a, self.b)
        self.time = time.perf_counter() - start
        return (self.identifier, self.x, self.time)

    def to_json(self) -> str:
        return json.dumps(
            {"a": self.a.tolist(), "b": self.b.tolist()}, sort_keys=True, indent=4
        )

    @staticmethod
    def from_json(text: str) -> "Task":
        j = json.loads(text)
        t = Task()
        t.a = np.array(j["a"])
        t.b = np.array(j["b"])
        return t

    def __eq__(self, other: "Task") -> bool:
        return np.array_equal(self.a, other.a) and np.array_equal(self.b, other.b)

    def __repr__(self):
        return str(self.a[0, 0])
