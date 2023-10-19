import consts
from string_operations import *
from image_operations import extract_bmp_pixels_as_rgb_bin, extract_completely_flatten_bmp_pixels, default_filename
from PIL import Image
import time


# Helper method for manipulating bits
# Inputs are e.g. flat_pixel_values [255, 0, 0, 255, 0, 0, 0, 255, 255, 0, 255, 255, 255, 0, 0, 255, 0, 0, 0, 255, 255, 0, 255, 255, 255, 0, 255, 255, 0, 255, 0, 255, 0, 0, 255, 0, 255, 0, 255, 255, 0, 255, 0, 255, 0, 0, 255, 0]
# str_as_bin e.g. "010000110100000101010100"
# n_bits_to_modify value between 1-4
# Output would be a list [242, 12, 2, 248, 10, 2, 0, 255, 255, 0, 255, 255, 255, 0, 0, 255, 0, 0, 0, 255, 255, 0, 255, 255, 255, 0, 255, 255, 0, 255, 0, 255, 0, 0, 255, 0, 255, 0, 255, 255, 0, 255, 0, 255, 0, 0, 255, 0]
def transform_image_with_message(flat_pixel_values, str_as_bin, n_bits_to_modify):
    bits_length = len(str_as_bin)
    break_outer = False
    current_bit_index_of_msg_bin = 0

    for i in range(len(flat_pixel_values)):
        for j in range(n_bits_to_modify):
            if str_as_bin[current_bit_index_of_msg_bin] == '1':
                flat_pixel_values[i] = flat_pixel_values[i] | (1 << j)
            else:
                flat_pixel_values[i] = flat_pixel_values[i] & ~(1 << j)

            current_bit_index_of_msg_bin = current_bit_index_of_msg_bin + 1
            if current_bit_index_of_msg_bin >= bits_length:
                break_outer = True
                break

        if break_outer:
            break

    print(f"Using {n_bits_to_modify} least significant bits, values transformed to:\n", flat_pixel_values)
    return flat_pixel_values


# The main method
# Input is an encoded string using the string_to_bits() method in string operations, filename and number of LSBs to modify
# Output is the new filename
def hide_message(message="Test", filename=default_filename, n_bits_to_modify=1):
    payload = f"{message}{consts.EXIT_STRING}"
    payload_list_of_bin = string_to_binary(payload)

    str_as_bin = "".join(payload_list_of_bin)
    bits_length = len(str_as_bin)

    try:
        header_info, img_size, flat_pixel_values = extract_completely_flatten_bmp_pixels(filename)
    except Exception as e:
        return str(e)

    width = img_size[0]
    height = img_size[1]
    print("RGB values before", flat_pixel_values)

    # validate number of bits to modify and lengths will fit
    if n_bits_to_modify > 4 or n_bits_to_modify < 1:
        print("A maximum of 4 least significant bits is supported to avoid too much image distortion. Also a minimum of 1.")
        return

    # validate message payload will fit
    if bits_length > n_bits_to_modify * len(flat_pixel_values):
        print(f"You have {bits_length} to encode but only {n_bits_to_modify * len(flat_pixel_values)} available.")
        return

    # Modify your flat pack of pixel values here
    flat_pixel_values = transform_image_with_message(flat_pixel_values, str_as_bin, n_bits_to_modify)

    # Save your flat pack of image values to an image
    new_image = Image.new("RGB", img_size)
    for y in range(height):
        for x in range(width):
            index = (y * width + x) * 3  # Each RGB triplet has 3 values
            rgb_values = flat_pixel_values[index:index + 3]  # Extract the RGB triplet
            new_image.putpixel((x, y), tuple(rgb_values))  # Convert the list to a tuple

    # Save the image
    # TODO mkdir for output_images
    output_filename = "output_images/" + str(int(time.time())) + "_output_test.bmp"
    new_image.save(output_filename)
    return output_filename


# Test main
if __name__ == "__main__":
    # Create a image using defaults
    new_file = hide_message()
    print(new_file)

    second_file = hide_message("CAT", default_filename, 2)
    print(second_file)
