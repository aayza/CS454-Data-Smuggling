from string_operations import *
from image_operations import extract_bmp_pixels_as_rgb_bin, extract_completely_flatten_bmp_pixels, default_filename
from PIL import Image
import time


def hide_message(message_list_of_bin=None, filename=default_filename, n_bits_to_modify=1):
    if message_list_of_bin is None:
        message_list_of_bin = ["01001101", "01000101", "01001111", "01010111"]

    str_as_bin = "".join(message_list_of_bin)
    bits_length = len(str_as_bin)
    print(str_as_bin)
    current_bit_index = 0

    header_info, img_size, flat_pixel_values = extract_completely_flatten_bmp_pixels(filename)
    width = img_size[0]
    height = img_size[1]
    print(len(flat_pixel_values), flat_pixel_values)

    # validate lengths will fit
    if bits_length > n_bits_to_modify * len(flat_pixel_values):
        print(f"You have {bits_length} to encode but only {n_bits_to_modify * len(flat_pixel_values)} available.")
        return

    # Modify your flat pack here
    for i in range(len(flat_pixel_values)):
        if n_bits_to_modify >= 1:
            if str_as_bin[current_bit_index] == '1':
                flat_pixel_values[i] = flat_pixel_values[i] | (1 << 0)
            else:
                flat_pixel_values[i] = flat_pixel_values[i] & ~(1 << 0)

            current_bit_index = current_bit_index + 1
            if current_bit_index >= bits_length:
                break

        if n_bits_to_modify >= 2:
            if str_as_bin[current_bit_index] == '1':
                flat_pixel_values[i] = flat_pixel_values[i] | (1 << 1)
            else:
                flat_pixel_values[i] = flat_pixel_values[i] & ~(1 << 1)

            current_bit_index = current_bit_index + 1
            if current_bit_index >= bits_length:
                break

        if n_bits_to_modify >= 3:
            if str_as_bin[current_bit_index] == '1':
                flat_pixel_values[i] = flat_pixel_values[i] | (1 << 2)
            else:
                flat_pixel_values[i] = flat_pixel_values[i] & ~(1 << 2)

            current_bit_index = current_bit_index + 1
            if current_bit_index >= bits_length:
                break

        if n_bits_to_modify >= 4:
            if str_as_bin[current_bit_index] == '1':
                flat_pixel_values[i] = flat_pixel_values[i] | (1 << 3)
            else:
                flat_pixel_values[i] = flat_pixel_values[i] & ~(1 << 3)

            current_bit_index = current_bit_index + 1
            if current_bit_index >= bits_length:
                break

    print(flat_pixel_values)

    # save your flat pack to an image
    new_image = Image.new("RGB", img_size)
    for y in range(height):
        for x in range(width):
            index = (y * width + x) * 3  # Each RGB triplet has 3 values
            rgb_values = flat_pixel_values[index:index + 3]  # Extract the RGB triplet
            new_image.putpixel((x, y), tuple(rgb_values))  # Convert the list to a tuple

    # Show or save the image
    new_image.show()
    output_filename = "output_images/" + str(int(time.time())) + "_output_test.bmp"
    new_image.save(output_filename)
    return output_filename


if __name__ == "__main__":
    new_file = hide_message()
    print(new_file)
    print(extract_bmp_pixels_as_rgb_bin(new_file))

    message = "CAT"
    message_in_bin = string_to_binary(message)

    second_file = hide_message(message_in_bin, default_filename, 4)
    print(second_file)
    print(extract_bmp_pixels_as_rgb_bin(second_file))
