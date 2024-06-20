import unittest
import random
from utils import drop_chars, move_whitespaces

class TestMoveWhitespaces(unittest.TestCase):
    def setUp(self):
        self.input_string = "This is a test string"
        random.seed(10)  # for deterministic results

    def test_empty_string(self):
        result, swaps = move_whitespaces("", 0.5)
        self.assertEqual(result, "")
        self.assertEqual(swaps, 0)

    def test_string_no_whitespaces(self):
        result, swaps = move_whitespaces("TestString", 0.5)
        self.assertEqual(result, "TestString")
        self.assertEqual(swaps, 0)

    def test_fraction_zero(self):
        result, swaps = move_whitespaces(self.input_string, 0)
        self.assertEqual(result, self.input_string)
        self.assertEqual(swaps, 0)

    def test_fraction_one(self):
        result, swaps = move_whitespaces(self.input_string, 1)
        self._test_common(result, self.input_string, swaps)

    def test_odd_whitespace_odd_length(self):
        result, swaps  = move_whitespaces("This is a test string ", 0.5,)
        self._test_common(result, "This is a test string ", swaps)

    def test_even_whitespace_odd_length(self):
        result, swaps = move_whitespaces("This is a test  string", 0.5)
        self._test_common(result, "This is a test  string", swaps)

    def test_odd_whitespace_even_length(self):
        result, swaps = move_whitespaces("This is a test string  ", 0.5)
        self._test_common(result, "This is a test string  ", swaps)

    def test_even_whitespace_even_length(self):
        result, swaps = move_whitespaces("This is a test  string  ", 0.5)
        self._test_common(result, "This is a test  string  ", swaps)

    def _test_common(self, result, input_str, expected_swaps):
        self.assertIsInstance(result, str)
        self.assertEqual(len(result), len(input_str))
        self.assertNotEqual(result, input_str)
        # swapped = sum(1 for c1, c2 in zip(input_str, result) if c1 != c2)
        # self.assertEqual(swapped/2, expected_swaps)

        self.assertEqual(result.replace(" ", ""), input_str.replace(" ", ""))
        print(result)

class TestDropPercentageCharacters(unittest.TestCase):

    def test_drop_chars(self):
        # test dropping 0%
        self.assertEqual(drop_chars("hello world", 0.0), "hello world")

        # test dropping 100%
        self.assertEqual(drop_chars("hello world", 1.0), "")

        # test dropping a realistic percentage
        original = "hello world"
        N = 0.6
        result = drop_chars(original, N)
        self.assertTrue(0 <= len(result) <= len(original))
        self.assertTrue(all(char in original for char in result))  # all chars in result should be in the original string
        expected_length = len(original) - round(len(original) * N)
        self.assertTrue(abs(len(result) - expected_length) <= 1)  # Allow tolerance for rounding

        # test dropping an invalid percentage
        with self.assertRaises(ValueError):
            drop_chars("hello world", -1)

        with self.assertRaises(ValueError):
            drop_chars("hello world", 101)



if __name__ == "__main__":
    unittest.main()