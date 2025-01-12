from Solution import Solution
from timeout_decorator import timeout
import unittest

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__testcases = {1: ('110', [1,1,3]), 2: ('001011', [11,8,5,4,3,4])}
        self.__obj = Solution()
        return super().setUp()

    @timeout(0.5)
    def test_case_1(self):
        boxes, output = self.__testcases[1]
        result = self.__obj.minOperations(boxes = boxes)
        self.assertIsInstance(result, list)
        self.assertTrue(all(r == o for r, o in zip(result, output)))

    @timeout(0.5)
    def test_case_2(self):
        boxes, output = self.__testcases[2]
        result = self.__obj.minOperations(boxes = boxes)
        self.assertIsInstance(result, list)
        self.assertTrue(all(r == o for r, o in zip(result, output)))

if __name__ == '__main__': unittest.main()