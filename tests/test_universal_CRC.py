import unittest

from universalCRC import crc

class TestCRC(unittest.TestCase):

    def test_CRC8_custom(self):
        self.assertEqual(crc.compute_CRC("313233343536373839",0x07,0xFF,0xAA,8,False,False),0x51)

    def test_CRC16_custom(self):
        self.assertEqual(crc.compute_CRC("313233343536373839",0x4845,0xFFFF,0x1415,16,False,False),0x4F23)

    def test_CRC32_custom(self):
        self.assertEqual(crc.compute_CRC("313233343536373839",0x14151232,0xFFFFFFFF,0x84A844B7,32,False,False),0x7BD8F91B)

    def test_CRC64_custom(self):
        self.assertEqual(crc.compute_CRC("313233343536373839",0x5643164643446516,0xFFFFFFFFFFFFFFFF,0x4164168ABDFEFFFD,64,False,False),0xD833BF285A1EBBFD)

    def test_CRC_preset(self):
        self.assertEqual(crc.compute_CRC("313233343536373839",preset="DARC"),0x15)

if __name__ == '__main__':
    unittest.main()