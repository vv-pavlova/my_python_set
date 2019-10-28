from MySet import MySet
import unittest
import string

class TestMySet(unittest.TestCase):
    
    def test_ASCIIs(self):
        testSet = MySet()
        for s in string.ascii_letters:
            testSet.add_value(s)
        res = ''.join(testSet.print_set())
        self.assertEqual(''.join(sorted(res)), ''.join(sorted(string.ascii_letters)))

    def test_collisions(self):
        testSet = MySet()
        input = [3, 14, 25, 36, 47, 58, 69, 80, 91, 102, 113, 124, 135, 146, 157, 168, 179, 190, 201, 212, 223, 234, 245, 256, 267, 278, 289, 300]
        for i in input:
            testSet.add_value(i)
        res = list(testSet.print_set())
        res.sort()
        self.assertEqual(res, input)
    
    def test_Delete(self):
        testSet = MySet()
        input = [3, 14, 25, 36, 47, 58, 69, 80, 91, 102, 113, 124, 135, 146, 157, 168, 179, 190, 201, 212, 223, 234, 245, 256, 267, 278, 289, 300]

        for i in input:
            testSet.add_value(i)

        res = list(testSet.print_set())
        res.sort()
        self.assertEqual(res, input)

        for i in input:
            testSet.del_value(i)

        self.assertEqual(testSet.print_set(), [])

if __name__ == '__main__':
    unittest.main()
