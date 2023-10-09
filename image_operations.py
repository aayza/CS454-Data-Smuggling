from PIL import Image
import time
from string_operations import *

default_filename = "input_images/test.bmp"

# Input is a BMP, output will be 5 variables. E.g.
# Header {'dpi': (299.9992380004115, 299.9992380004115), 'compression': 0}
# Image size (4, 4)
# Red channel   [[255, 255, 0, 0], [255, 255, 0, 0], [255, 255, 0, 0], [255, 255, 0, 0]]
# Green channel [[0, 0, 255, 255], [0, 0, 255, 255], [0, 0, 255, 255], [0, 0, 255, 255]]
# Blue channel  [[0, 0, 255, 255], [0, 0, 255, 255], [255, 255, 0, 0], [255, 255, 0, 0]]
# Unused method, kept for investigation purposes
def extract_bmp_channels_ints(filename = default_filename):
    red_channel = []
    green_channel = []
    blue_channel = []

    try:
        with Image.open(filename) as img:
            header = img.info
            width, height = img.size
            # iterating through from top row and across
            for y in range(height):
                red_row = []
                green_row = []
                blue_row = []

                for x in range(width):
                    r, g, b = img.getpixel((x, y))

                    red_row.append(r)
                    green_row.append(g)
                    blue_row.append(b)

                red_channel.append(red_row)
                green_channel.append(green_row)
                blue_channel.append(blue_row)

            return header, img.size, red_channel, green_channel, blue_channel
    except Exception as e:
        return str(e)

# Input is a BMP file
# Output is e.g.
# Header {'dpi': (299.9992380004115, 299.9992380004115), 'compression': 0}
# Image size (4, 4)
# Red [['11111111', '11111111', '00000000', '00000000'], ['11111111', '11111111', '00000000', '00000000'], ['11111111', '11111111', '00000000', '00000000'], ['11111111', '11111111', '00000000', '00000000']]
# Green [['00000000', '00000000', '11111111', '11111111'], ['00000000', '00000000', '11111111', '11111111'], ['00000000', '00000000', '11111111', '11111111'], ['00000000', '00000000', '11111111', '11111111']]
# Blue [['00000000', '00000000', '11111111', '11111111'], ['00000000', '00000000', '11111111', '11111111'], ['00000000', '00000000', '11111111', '11111111'], ['00000000', '00000000', '11111111', '11111111']]
# Unused method, kept for investigation purposes
def extract_bmp_channels_bin(filename = default_filename):
    header, img_size, red_channel, green_channel, blue_channel = extract_bmp_channels_ints(filename)

    red_as_binary = [[bin(num)[2:].zfill(8) for num in sublistrow] for sublistrow in red_channel]
    green_as_binary = [[bin(num)[2:].zfill(8) for num in sublistrow] for sublistrow in green_channel]
    blue_as_binary = [[bin(num)[2:].zfill(8) for num in sublistrow] for sublistrow in green_channel]

    return header, img_size, red_as_binary, green_as_binary, blue_as_binary

# Input is a BMP file
# Output is triplets of ints in a matrix form, e.g.
# RGB pixels [[[255, 0, 0], [255, 0, 0], [0, 255, 255], [0, 255, 255]], [[255, 0, 0], [255, 0, 0], [0, 255, 255], [0, 255, 255]], [[255, 0, 255], [255, 0, 255], [0, 255, 0], [0, 255, 0]], [[255, 0, 255], [255, 0, 255], [0, 255, 0], [0, 255, 0]]]
# Unused method, kept for investigation purposes
def extract_bmp_pixels_as_rgb_int(filename = default_filename):
    output = []

    try:
        with Image.open(filename) as img:
            header = img.info
            width, height = img.size
            # iterating through from top row and across
            for y in range(height):
                current_row = []

                for x in range(width):
                    [r, g, b] = img.getpixel((x, y))
                    current_row.append([r,g, b])

                output.append(current_row)

            return header, img.size, output
    except Exception as e:
        return str(e)

# Input is BMP file
# Output is tuples of binary, e.g.
# RGB pixels as bin [[['11111111', '00000000', '00000000'], ['11111111', '00000000', '00000000'], ['00000000', '11111111', '11111111'], ['00000000', '11111111', '11111111']], [['11111111', '00000000', '00000000'], ['11111111', '00000000', '00000000'], ['00000000', '11111111', '11111111'], ['00000000', '11111111', '11111111']], [['11111111', '00000000', '11111111'], ['11111111', '00000000', '11111111'], ['00000000', '11111111', '00000000'], ['00000000', '11111111', '00000000']], [['11111111', '00000000', '11111111'], ['11111111', '00000000', '11111111'], ['00000000', '11111111', '00000000'], ['00000000', '11111111', '00000000']]]
# Unused method, kept for investigation purposes
def extract_bmp_pixels_as_rgb_bin(filename = default_filename):
    header_info, img_size, output = extract_bmp_pixels_as_rgb_int(filename)
    new_output_as_bin = [
        [
            [bin(value)[2:].zfill(8) for value in rgb_triplet]
            for rgb_triplet in row
        ]
        for row in output
    ]
    return header_info, img_size, new_output_as_bin

# Input is a bmp file
# Output is RGB triplets in the following format: [[1, 2, 3], [10, 20, 30], [100, 200, 300]] etc
# Unused method, kept for investigation purposes
def extract_and_flatten_bmp_pixels_as_rgb_int_triplets(filename = default_filename):
    output = []

    try:
        with Image.open(filename) as img:
            header = img.info
            width, height = img.size
            # iterating through from top row and across
            for y in range(height):

                for x in range(width):
                    [r, g, b] = img.getpixel((x, y))
                    output.append([r, g, b])

            return header, img.size, output
    except Exception as e:
        return str(e)

# Input is a bmp file
# Output is a single flat list of repeating RGB values: [1, 2, 3, 10, 20, 30, 100, 200, 300] etc
# This method is used
def extract_completely_flatten_bmp_pixels(filename = default_filename):
    output = []

    try:
        with Image.open(filename) as img:
            header = img.info
            width, height = img.size
            # iterating through from top row and across
            for y in range(height):

                for x in range(width):
                    r, g, b = img.getpixel((x, y))
                    output.append(r)
                    output.append(g)
                    output.append(b)

            return header, img.size, output
    except Exception as e:
        return str(e)

# Helper method for encoding, image must be a reference to an image copy
# new_colour is a triplet tuple, e.g. (255, 0, 0)
# Do not use this, completely obsolete
def set_pixel_colour(image, x, y, new_colour):
    try:
        image.putpixel((x,y), new_colour)
    except Exception as e:
        return str(e)

# Test main
if __name__ == "__main__":
    header_info, img_size, red_channel, green_channel, blue_channel = extract_bmp_channels_ints()

    print("Header", header_info)
    print("Image size", img_size)
    print("Red channel  ", red_channel)
    print("Green channel", green_channel)
    print("Blue channel ", blue_channel)

    header_info, img_size, red_as_binary, green_as_binary, blue_as_binary = extract_bmp_channels_bin()
    print("Red", red_as_binary)
    print("Green", green_as_binary)
    print("Blue", blue_as_binary)

    # As RGB per pixel
    header_info, img_size, output = extract_bmp_pixels_as_rgb_int()
    print("Header", header_info)
    print("Image size", img_size)
    print("RGB pixels", output)

    header_info, img_size, output = extract_bmp_pixels_as_rgb_bin()
    print("RGB pixels as bin", output)

    print("flat pack", extract_and_flatten_bmp_pixels_as_rgb_int_triplets())
    print("completely flat pack", extract_completely_flatten_bmp_pixels())

    # set new colour of pixel 0, 0 of the test image
    with Image.open(default_filename) as img:
        modified_image = img.copy()
        set_pixel_colour(modified_image, 0, 0, (0, 0, 255))
        modified_image.save("output_images/" + str(int(time.time())) + "_output_test.bmp")