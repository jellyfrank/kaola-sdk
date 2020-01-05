import unittest
from kaola.api.kaola import KaoLa

class TestOrder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.kl = KaoLa("edb6c3b9ac4847e7584c38e2b630b14f", "8200ee92ec22fcae76e2f00bc5c79247188e0593",
                       access_token="b658b654-6d13-4a3e-8350-e427949a9641", sandbox=True)

    def test_order(self):
        """
        测试订单
        """
        res = self.kl.order.search_order(
            2, 1, "2019-11-07 00:20:48", "2019-12-31 11:20:48")
        self.assertTrue(res.get("total_count", None), res)

    def test_get_order(self):
        """
        测试获取订单详情
        """
        res = self.kl.order.get_order("2019121223191084536337814")
        self.assertTrue(res.get("order", None), res)


if __name__ == "__main__":
    unittest.main()
