import unittest
from action import *


class action_test(unittest.TestCase):
    def test_something(self):
        action = WorkoutAction("what is a if statement")
        self.assertTrue(isinstance(action, WorkoutAction))


if __name__ == '__main__':
    unittest.main()
