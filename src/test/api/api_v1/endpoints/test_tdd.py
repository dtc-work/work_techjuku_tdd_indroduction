import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../app')))

class TestArrayOperations(unittest.TestCase):
    def test_配列を受け取りその配列を返す(self):
        array = ArrayOperations([16,12,24])
        assert [16,12,24] == array.raw()

if __name__ == "__main__":
    unittest.main()
