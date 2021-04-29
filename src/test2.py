import unittest
import sample

class TestCaculatorMethods(unittest.TestCase):
    def test_substrac(self):
        ca = sample.Caculator(4,2)
        self.assertEqual(2,ca.substrac())
    def test_multiply(self):
        ca = sample.Caculator(2,5)
        self.assertEqual(10,ca.multiply())

if __name__ == '__main__':
    unittest.main()
