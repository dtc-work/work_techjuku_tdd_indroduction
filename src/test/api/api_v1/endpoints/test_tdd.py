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

    def test_配列の中身に奇数が含まれていればfalseを返す(self):
        array = ArrayOperations([16,12,25])
        assert False == array.is_all_even()

    def test_配列の中身が全て偶数であれば要素を全て2で割ったものに置き換えて返す(self):
        array = ArrayOperations([16,12,24])
        assert [8,6,12] == array.divided_by_2()

    def test_配列の中身に奇数が含まれていればそのまま返す(self):
        array = ArrayOperations([16,12,25])
        assert [16,12,25] == array.divided_by_2()

if __name__ == "__main__":
    unittest.main()
