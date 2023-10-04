import os
import unittest
from PIL import Image
import time

from image_operations import *
from hiding_message import *
from string_operations import *


# String operations unit tests

class TestStringConversionFunctions(unittest.TestCase):
    def test_string_to_binary(self):
        input_str = "ABC"
        expected_output = ["01000001", "01000010", "01000011"]
        self.assertEqual(string_to_binary(input_str), expected_output)

    def test_binary_to_string(self):
        input_binary_str_list = ["01000001", "01000010", "01000011"]
        expected_output = "ABC"
        self.assertEqual(binary_to_string(input_binary_str_list), expected_output)

    def test_string_to_char_ints(self):
        input_str = "ABC"
        expected_output = [65, 66, 67]
        self.assertEqual(string_to_char_ints(input_str), expected_output)

    def test_ints_list_to_str(self):
        input_int_list = [65, 66, 67]
        expected_output = "ABC"
        self.assertEqual(ints_list_to_str(input_int_list), expected_output)


# Image operations unit tests
class TestBMPProcessingFunctions(unittest.TestCase):

    def setUp(self):
        self.test_image = "input_images/test.bmp"



# Hiding messages/encoding unit tests

class TestHideMessageFunction(unittest.TestCase):

    def setUp(self):
        self.test_image = "input_images/test.bmp"
        self.output_folder = "output_images"

    def reset(self):
        for filename in os.listdir(self.output_folder):
            file_path = os.path.join(self.output_folder, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)




# Finding messages/decoding unit tests
# TO DO

if __name__ == '__main__':
    unittest.main()
