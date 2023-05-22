import unittest

from src._05_2023._22_05_2023.is_bool import is_bool
from src._05_2023._22_05_2023.is_twin import is_twin


class Test_Solution(unittest.TestCase):
    def test_is_bool(self):
        self.assertTrue(is_bool(1, 5))
        self.assertFalse(is_bool(2, 3))
        self.assertTrue(is_bool(-3, 4))

    def test_is_twin(self):
        self.assertTrue(is_twin("Marion", "Romain"))


if __name__ == "__main__":
    unittest.main()
