import unittest


class UnittestExample(unittest.TestCase):
    def setUp(self):
        print('Join to setUp')
        self.list = [0, 1, 5, 8]

    def tearDown(self):
        print('Join to tear down')

    def test_01(self):
        print('Join to test_01')
        ls = [0, 1, 5, 8]
        self.assertEqual(ls, self.list)
