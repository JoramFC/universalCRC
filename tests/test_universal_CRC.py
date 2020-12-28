import unittest

from src import universalCRC

class TestCRC(unittest.TestCase):

    def test_CRC8(self):
        self.assertEqual(universalCRC.compute_CRC("313233343536373839",0x07,0x00,8),0xF4)

if __name__ == '__main__':
    unittest.main()