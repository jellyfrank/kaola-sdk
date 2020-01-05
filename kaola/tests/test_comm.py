
import unittest
from kaola.api.kaola import KaoLa


class TestComm(unittest.TestCase):

    def test_sign(self):
        """
        测试签名算法
        """
        kaola = KaoLa("my-client", "clientSecret")
        data = {
            "access_token": "c9aadff0-8ee9-43ef-8cbc-59be572c0c2f",
            "timestamp": "2015-12-02 10:16:16",
            "method": "kaola.common.provinces.get"
        }

        self.assertEqual(kaola.comm.sign(
            data), "38CE64C36579F93799083D8A7F9CB33E")


if __name__ == "__main__":
    unittest.main()
