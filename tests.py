import unittest
import Counter

class TestBowlingScore(unittest.TestCase):

    def test_normal_score(self):
        throws = [3, 5, 2, 4, 1, 3, 8, 1, 7, 2, 4, 5, 6, 2, 3, 1, 4, 5, 2, 3]
        self.assertEqual(Counter.bowling_score(throws), sum(throws))

    def test_strike_followed_by_spare(self):
        throws = [10, 5, 5, 3, 4, 2, 7, 1, 8, 0, 6, 2, 9, 0, 7, 3, 10, 3, 6]
        self.assertEqual(Counter.bowling_score(throws), 104)

    def test_all_strikes(self):
        throws = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        self.assertEqual(Counter.bowling_score(throws), 300)

    def test_all_spares(self):
        throws = [5, 5, 6, 4, 7, 3, 8, 2, 9, 1, 5, 5, 8, 2, 4, 6, 7, 3, 9, 1, 10]
        self.assertEqual(Counter.bowling_score(throws), 173)

    def test_invalid_throw_value(self):
        throws = [3, 5, 2, 4, 11, 3, 8, 1, 7, 2, 4, 5, 6, 2, 3, 1, 4, 5, 2, 3]
        with self.assertRaises(ValueError):
            Counter.bowling_score(throws)

    def test_valid_max_throw(self):
        throws = [1, 2, 10, 9, 10, 10, 20, 0, 19, 1]
        self.assertEqual(Counter.bowling_score(throws, max_pins=20), 121)

    def test_invalid_max_throw(self):
        throws = [1, 2, 5, 9, 1, 2, 5, 0, 2, 1]
        with self.assertRaises(ValueError):
            Counter.bowling_score(throws, max_pins=5)

if __name__ == '__main__':
    unittest.main()
