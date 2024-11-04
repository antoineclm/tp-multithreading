import unittest
import numpy
from task import Task


class TestTask(unittest.TestCase):
    def test_task(self):
        t = Task()
        numpy.testing.assert_allclose(t.a @ t.bx, t.b)


if __name__ == "__main__":
    unittest.main()
