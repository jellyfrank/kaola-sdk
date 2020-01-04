
import unittest
from kaola.api.kaola import KaoLa


class TestBasic(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.kl = KaoLa("edb6c3b9ac4847e7584c38e2b630b14f",
                       "8200ee92ec22fcae76e2f00bc5c79247188e0593", sandbox=True)

    def test_get_access_token(self):
        print(self.kl.generate_authorization_code_url("192.168.1.1"))

    def test_get_taxnos(self):
        print(self.kl.basic.get_taxnos())


if __name__ == "__main__":
    unittest.main()
