from PIL import Image
import time

default_filename = "input_images/test.bmp"

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
                    (r, g, b) = img.getpixel((x, y))
                    current_row.append((r,g, b))

                output.append(current_row)

            return header, img.size, output
    except Exception as e:
        return str(e)

def extract_bmp_pixels_as_rgb_bin(filename = default_filename):
    header_info, img_size, output = extract_bmp_pixels_as_rgb_int(filename)
    new_output_as_bin = [
        [
            tuple(bin(value)[2:].zfill(8) for value in rgb_tuple)
            for rgb_tuple in row
        ]
        for row in output
    ]
    return header_info, img_size, new_output_as_bin

# Helper method for encoding, image must be a reference to an image copy
# new_colour is a triplet tuple, e.g. (255, 0, 0)
def set_pixel_colour(image, x, y, new_colour):
    try:
        image.putpixel((x,y), new_colour)
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    header_info, img_size, red_channel, green_channel, blue_channel = extract_bmp_channels_ints()

    print("Header", header_info)
    print("Image size", img_size)
    print("Red channel  ", red_channel)
    print("Green channel", green_channel)
    print("Blue channel ", blue_channel)

    # As binary strings
    red_as_binary = [[bin(num)[2:] for num in sublistrow] for sublistrow in red_channel]
    green_as_binary = [[bin(num)[2:] for num in sublistrow] for sublistrow in green_channel]
    blue_as_binary = [[bin(num)[2:] for num in sublistrow] for sublistrow in green_channel]
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

    # set new colour of pixel 0, 0 of the test image
    with Image.open(default_filename) as img:
        modified_image = img.copy()
        set_pixel_colour(modified_image, 0, 0, (0, 0, 255))
        modified_image.save("output_images/" + str(int(time.time())) + "_output_test.bmp")

        [
            [(255, 0, 0), (255, 0, 0), (0, 255, 255), (0, 255, 255)],
            [(255, 0, 0), (255, 0, 0), (0, 255, 255), (0, 255, 255)]
        ]