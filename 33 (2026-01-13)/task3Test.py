import unittest
from task1 import stringToList

class TestTask1(unittest.TestCase):
    def setUp(self):
        self.strInput = "4th generation jet fighter"
    def testSplitting(self):
        self.assertEqual(stringToList(self.strInput), ['4th', 'generation', 'jet', 'fighter'])

    @unittest.skip("skipping")
    def testIfEmpty(self):
        self.assertEqual(stringToList(''), [])

    def testIfInt(self):
        with self.assertRaises(TypeError):
            stringToList(1)

    @unittest.expectedFailure
    def testFailure(self):
        self.assertEqual(stringToList('Hello world'), [])

    def tearDown(self):
        del self.strInput


if __name__ == '__main__':
    unittest.main()