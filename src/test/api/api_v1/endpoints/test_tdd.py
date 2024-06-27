import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../app')))
from app.api.api_v1.endpoints.tdd import ArrayOperations


class TestArrayOperations(unittest.TestCase):
    def test_配列を受け取りその配列を返す(self):
        array = ArrayOperations([16,12,24])
        assert [16,12,24] == array.raw()

class TestIsAllEven(TestArrayOperations):
    def test_配列の中身が全て偶数であればtrueを返す(self):
        array = ArrayOperations([16,12,24])
        assert True == array.is_all_even([8,6,12])

    def test_配列の中身に奇数が含まれていればfalseを返す(self):
        array = ArrayOperations([16,12,24])
        assert False == array.is_all_even([4,3,6])

class TestNumberOfDividedTimes(TestArrayOperations):
    def test_配列の中身を2で割る操作を繰り返し操作できた回数を返す_16_12_24だと2回(self):
        array = ArrayOperations([16,12,24])
        assert 2 == array.number_of_divided_times()

    def test_配列の中身を2で割る操作を繰り返し操作できた回数を返す_16_12_25だと0回(self):
        array = ArrayOperations([16,12,25])
        assert 0 == array.number_of_divided_times()

if __name__ == "__main__":
    unittest.main()
