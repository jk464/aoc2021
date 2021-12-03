import unittest
import src

class TestStringMethods(unittest.TestCase):

    def test_day_01(self):
        with open("inputs/day_01/inputs.txt", "r") as file:
          self.inputs = [int(l) for l in file.readlines()]

        self.assertTrue(src.day_01.find_increase_count(self.inputs, window=1) == 1446)

if __name__ == '__main__':
    unittest.main()