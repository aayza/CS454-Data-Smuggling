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

    def test_extract_bmp_channels_ints(self):
        header, img_size, red_channel, green_channel, blue_channel = extract_bmp_channels_ints(self.test_image)
        self.assertEqual(img_size, (4, 4))
        self.assertEqual(len(red_channel), 4)
        self.assertEqual(len(green_channel), 4)
        self.assertEqual(len(blue_channel), 4)

    def test_extract_bmp_channels_bin(self):
        header, img_size, red_as_binary, green_as_binary, blue_as_binary = extract_bmp_channels_bin(
            self.test_image)
        self.assertEqual(img_size, (4, 4))
        self.assertEqual(len(red_as_binary), 4)
        self.assertEqual(len(green_as_binary), 4)
        self.assertEqual(len(blue_as_binary), 4)

    def test_extract_bmp_pixels_as_rgb_int(self):
        header, img_size, rgb_pixels = extract_bmp_pixels_as_rgb_int(self.test_image)
        self.assertEqual(img_size, (4, 4))
        self.assertEqual(len(rgb_pixels), 4)

    def test_extract_bmp_pixels_as_rgb_bin(self):
        header, img_size, rgb_pixels_as_bin = extract_bmp_pixels_as_rgb_bin(self.test_image)
        self.assertEqual(img_size, (4, 4))
        self.assertEqual(len(rgb_pixels_as_bin), 4)

    def test_extract_and_flatten_bmp_pixels_as_rgb_int_triplets(self):
        header, img_size, flattened_pixels = extract_and_flatten_bmp_pixels_as_rgb_int_triplets(self.test_image)
        self.assertEqual(img_size, (4, 4))
        self.assertEqual(len(flattened_pixels), 16)  # 4x4 = 16


    def test_extract_completely_flatten_bmp_pixels(self):
        header, img_size, flattened_pixels = extract_completely_flatten_bmp_pixels(self.test_image)
        self.assertEqual(img_size, (4, 4))
        self.assertEqual(len(flattened_pixels), 48)  # 4x4x3 = 48

    def test_set_pixel_colour(self):
        output_filename = "output_images/test_output.bmp"
        with Image.open(self.test_image) as img:
            modified_image = img.copy()
            set_pixel_colour(modified_image, 0, 0, (0, 0, 255))
            modified_image.save(output_filename)
        self.assertTrue(os.path.exists(output_filename))
        os.remove(output_filename)

        # testing pixels are different


# Hiding messages/encoding unit tests

class TestHideMessageFunction(unittest.TestCase):

    def setUp(self):
        self.test_image = "input_images/test.bmp"
        self.output_folder = "output_images"

    def tearDown(self):
        for filename in os.listdir(self.output_folder):
            file_path = os.path.join(self.output_folder, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)

    def test_hide_message_default(self):
        output_filename = hide_message()
        self.assertTrue(os.path.exists(output_filename))
        header_info, img_size, rgb_pixels_as_bin = extract_bmp_pixels_as_rgb_bin(output_filename)
        self.assertEqual(img_size, (4, 4))
        self.assertEqual(len(rgb_pixels_as_bin), 4)

    def test_hide_message_with_message(self):
        message = "CAT"
        message_in_bin = string_to_binary(message)
        output_filename = hide_message(message_in_bin, self.test_image, 4)
        self.assertTrue(os.path.exists(output_filename))
        header_info, img_size, rgb_pixels_as_bin = extract_bmp_pixels_as_rgb_bin(output_filename)
        self.assertEqual(img_size, (4, 4))
        self.assertEqual(len(rgb_pixels_as_bin), 4)


if __name__ == '__main__':
    unittest.main()
