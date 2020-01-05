
import unittest
from kaola.api.kaola import KaoLa


class TestBasic(unittest.TestCase):

    # fniki_1@163.com password：abc123
    # appKey：edb6c3b9ac4847e7584c38e2b630b14f
    # appSecret：8200ee92ec22fcae76e2f00bc5c79247188e0593

    @classmethod
    def setUpClass(cls):
        cls.kl = KaoLa("edb6c3b9ac4847e7584c38e2b630b14f",
                       "8200ee92ec22fcae76e2f00bc5c79247188e0593", access_token="b658b654-6d13-4a3e-8350-e427949a9641", sandbox=True)

    # def test_get_access_token(self):
    #     code = "8ywIwk&state=7CA94FF"
    #     # print(self.kl.generate_authorization_code_url("http://www.kaola.com"))
    #     print(self.kl.get_access_token(code, "http://www.kaola.com"))

    # def test_get_taxnos(self):
    #     print(self.kl.basic.get_taxnos())


if __name__ == "__main__":
    unittest.main()
