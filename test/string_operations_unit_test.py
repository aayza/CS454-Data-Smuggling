import unittest
from string_operations_unit_test import *


# String operations unit tests
class TestStringOperations(unittest.TestCase):
    def test_string_to_binary(self):
        input_str = "ABC"
        expected_output = ["01000001", "01000010", "01000011"]
        self.assertEqual(string_to_binary(input_str), expected_output)

    def test_binary_to_string(self):
        input_binary_str_list = ["01000001", "01000010", "01000011"]
        expected_output = "ABC"
        self.assertEqual(binary_to_string(input_binary_str_list), expected_output)

    def test_binary_string_to_string(self):
        input_binary_str = ["010000010100001001000011"]
        expected_output = "ABC"
        self.assertEqual(binary_string_to_string(input_binary_str), expected_output)

    def test_string_to_char_ints(self):
        input_str = "ABC"
        expected_output = [65, 66, 67]
        self.assertEqual(string_to_char_ints(input_str), expected_output)

    def test_ints_list_to_str(self):
        input_int_list = [65, 66, 67]
        expected_output = "ABC"
        self.assertEqual(ints_list_to_str(input_int_list), expected_output)

    def test_binary_to_byte_array(self):
        binary_string = "01000001001010101010101010101010"
        expected_result = ["01000001", "00101010", "10101010", "10101010"]
        self.assertEqual(binary_to_byte_array(binary_string), expected_result)


if __name__ == '__main__':
    unittest.main()
