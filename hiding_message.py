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
def hide_message(message_list_of_bin=None, filename=default_filename, n_bits_to_modify=1):
    if message_list_of_bin is None:
        message_list_of_bin = ["01001101", "01000101", "01001111", "01010111"] # default message

    str_as_bin = "".join(message_list_of_bin)
    bits_length = len(str_as_bin)
    print(f"Your message as a continuous string of 1s and 0s is: {str_as_bin}")


    header_info, img_size, flat_pixel_values = extract_completely_flatten_bmp_pixels(filename)
    width = img_size[0]
    height = img_size[1]
    print("RGB values before", flat_pixel_values)

    # validate number of bits to modify and lengths will fit
    if n_bits_to_modify > 4 or n_bits_to_modify < 1:
        print("Maximum of 4 least significant bits is supported to avoid too much image distortion. Also a minimum of 1.")
        return

    if bits_length > n_bits_to_modify * len(flat_pixel_values):
        print(f"You have {bits_length} to encode but only {n_bits_to_modify * len(flat_pixel_values)} available.")
        return

    # Modify your flat pack of pixel values here
    flat_pixel_values = transform_image_with_message(flat_pixel_values, str_as_bin, n_bits_to_modify)

    # save your flat pack of image values to an image
    new_image = Image.new("RGB", img_size)
    for y in range(height):
        for x in range(width):
            index = (y * width + x) * 3  # Each RGB triplet has 3 values
            rgb_values = flat_pixel_values[index:index + 3]  # Extract the RGB triplet
            new_image.putpixel((x, y), tuple(rgb_values))  # Convert the list to a tuple

    # Show and save the image
    new_image.show()
    output_filename = "output_images/" + str(int(time.time())) + "_output_test.bmp"
    new_image.save(output_filename)
    print("Image details after", extract_bmp_pixels_as_rgb_bin(output_filename))
    return output_filename

# Test main
if __name__ == "__main__":
    # Create a image using defaults
    new_file = hide_message()
    print(new_file)
    print(extract_bmp_pixels_as_rgb_bin(new_file))

    # Specify a custom message
    message = "CAT"
    message_in_bin = string_to_binary(message)

    second_file = hide_message(message_in_bin, default_filename, 4)
    print(second_file)
    print(extract_bmp_pixels_as_rgb_bin(second_file))
