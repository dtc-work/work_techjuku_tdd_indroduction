import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../app')))
from app.api.api_v1.endpoints.tdd import ArrayOperations


class TestArrayOperations(unittest.TestCase):
    def test_配列を受け取りその配列を返す(self):
        array = ArrayOperations([16,12,24])
        assert [16,12,24] == array.raw()

    def test_配列の中身が全て偶数であればtrueを返す(self):
        array = ArrayOperations([16,12,24])
        assert True == array.is_all_even()

if __name__ == "__main__":
    unittest.main()
