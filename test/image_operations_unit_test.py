import os
import unittest
from PIL import Image
from image_operations import *


# Image operations unit tests
class TestImageOperations(unittest.TestCase):

    def setUp(self):
        self.test_image = "../input_images/test.bmp"

    def test_extract_bmp_channels_ints(self):
        header, img_size, red_channel, green_channel, blue_channel = extract_bmp_channels_ints(self.test_image)
        self.assertEqual(img_size, (4, 4))
        # Assuming the test.bmp image
        self.assertEqual(len(red_channel), 4)
        self.assertEqual(len(green_channel), 4)
        self.assertEqual(len(blue_channel), 4)
        # test in len and actual colour format
        self.assertEqual(red_channel, [[255, 255, 0, 0], [255, 255, 0, 0], [255, 255, 0, 0], [255, 255, 0, 0]])
        self.assertEqual(green_channel, [[0, 0, 255, 255], [0, 0, 255, 255], [0, 0, 255, 255], [0, 0, 255, 255]])
        self.assertEqual(blue_channel, [[0, 0, 255, 255], [0, 0, 255, 255], [255, 255, 0, 0], [255, 255, 0, 0]])

    def test_extract_bmp_channels_bin(self):
        header, img_size, red_as_binary, green_as_binary, blue_as_binary = extract_bmp_channels_bin(
            self.test_image)
        self.assertEqual(img_size, (4, 4))
        self.assertEqual(len(red_as_binary), 4)
        self.assertEqual(len(green_as_binary), 4)
        self.assertEqual(len(blue_as_binary), 4)
        # test in len and actual colour format
        self.assertEqual(red_as_binary, [['11111111', '11111111', '00000000', '00000000'],
                                         ['11111111', '11111111', '00000000', '00000000'],
                                         ['11111111', '11111111', '00000000', '00000000'],
                                         ['11111111', '11111111', '00000000', '00000000']])
        self.assertEqual(green_as_binary, [['00000000', '00000000', '11111111', '11111111'],
                                           ['00000000', '00000000', '11111111', '11111111'],
                                           ['00000000', '00000000', '11111111', '11111111'],
                                           ['00000000', '00000000', '11111111', '11111111']])
        self.assertEqual(blue_as_binary, [['00000000', '00000000', '11111111', '11111111'],
                                          ['00000000', '00000000', '11111111', '11111111'],
                                          ['00000000', '00000000', '11111111', '11111111'],
                                          ['00000000', '00000000', '11111111', '11111111']])

    def test_extract_bmp_pixels_as_rgb_int(self):
        header, img_size, rgb_pixels = extract_bmp_pixels_as_rgb_int(self.test_image)
        self.assertEqual(img_size, (4, 4))
        self.assertEqual(len(rgb_pixels), 4)

        expected_output = [[[255, 0, 0], [255, 0, 0], [0, 255, 255], [0, 255, 255]],
                           [[255, 0, 0], [255, 0, 0], [0, 255, 255], [0, 255, 255]],
                           [[255, 0, 255], [255, 0, 255], [0, 255, 0], [0, 255, 0]],
                           [[255, 0, 255], [255, 0, 255], [0, 255, 0], [0, 255, 0]]]

        self.assertEqual(rgb_pixels, expected_output)

    def test_extract_bmp_pixels_as_rgb_bin(self):
        header, img_size, rgb_pixels_as_bin = extract_bmp_pixels_as_rgb_bin(self.test_image)
        self.assertEqual(img_size, (4, 4))
        self.assertEqual(len(rgb_pixels_as_bin), 4)

        expected_output = [[['11111111', '00000000', '00000000'], ['11111111', '00000000', '00000000'],
                            ['00000000', '11111111', '11111111'], ['00000000', '11111111', '11111111']],
                           [['11111111', '00000000', '00000000'], ['11111111', '00000000', '00000000'],
                            ['00000000', '11111111', '11111111'], ['00000000', '11111111', '11111111']],
                           [['11111111', '00000000', '11111111'], ['11111111', '00000000', '11111111'],
                            ['00000000', '11111111', '00000000'], ['00000000', '11111111', '00000000']],
                           [['11111111', '00000000', '11111111'], ['11111111', '00000000', '11111111'],
                            ['00000000', '11111111', '00000000'], ['00000000', '11111111', '00000000']]]

        self.assertEqual(rgb_pixels_as_bin, expected_output)

    def test_extract_and_flatten_bmp_pixels_as_rgb_int_triplets(self):
        header, size, flattened_pixels = extract_and_flatten_bmp_pixels_as_rgb_int_triplets(self.test_image)
        self.assertEqual(size, (4, 4))
        self.assertEqual(len(flattened_pixels), 16)  # 4x4 = 16

        expected_output = [[255, 0, 0], [255, 0, 0], [0, 255, 255], [0, 255, 255], [255, 0, 0], [255, 0, 0],
                           [0, 255, 255], [0, 255, 255],
                           [255, 0, 255], [255, 0, 255], [0, 255, 0], [0, 255, 0], [255, 0, 255], [255, 0, 255],
                           [0, 255, 0], [0, 255, 0]]
        self.assertEqual(flattened_pixels, expected_output)

    def test_extract_completely_flatten_bmp_pixels(self):
        header, img_size, flattened_pixels = extract_completely_flatten_bmp_pixels(self.test_image)
        self.assertEqual(img_size, (4, 4))
        self.assertEqual(len(flattened_pixels), 48)  # 4x4x3 = 48

        expected_output = [255, 0, 0, 255, 0, 0, 0, 255, 255, 0, 255, 255, 255, 0, 0, 255, 0, 0, 0, 255, 255, 0, 255,
                           255, 255, 0, 255, 255, 0, 255, 0, 255, 0, 0, 255, 0, 255, 0, 255, 255, 0, 255, 0, 255, 0, 0,
                           255, 0]

        self.assertEqual(flattened_pixels, expected_output)

    def test_set_pixel_colour(self):
        output_filename = "../output_images/test.bmp"
        with Image.open(self.test_image) as img:
            modified_image = img.copy()
            set_pixel_colour(modified_image, 0, 0, (0, 0, 255))
            modified_image.save(output_filename)
        self.assertTrue(os.path.exists(output_filename))
        os.remove(output_filename)
        # testing pixels are different


if __name__ == '__main__':
    unittest.main()
