from string_operations import *
from image_operations import *

def hide_message(message_list_of_bin = ["01000001","01000010","01000011"], filename = default_filename, n_bits_to_modify = 1):
    str_as_bin = "".join(message_list_of_bin)
    bits_length = len(str_as_bin)
    print(str_as_bin)
    current_bit_index = 0

    header_info, img_size, flat_pixel_values = extract_completely_flatten_bmp_pixels()
    width = img_size[0]
    height = img_size[1]
    print(len(flat_pixel_values), flat_pixel_values)

    # validate lengths will fit
    if bits_length > n_bits_to_modify * len(flat_pixel_values):
        print(f"You have {bits_length} to encode but only {n_bits_to_modify * len(flat_pixel_values)} available.")
        return

    # Modify your flat pack here
    for x in flat_pixel_values:
        if current_bit_index >= bits_length:
            break;

        if n_bits_to_modify >= 1:
            if str_as_bin[current_bit_index] == '1':
                x = x | (1 << 1)
            else:
                x = x & ~(1 << 1)

            current_bit_index = current_bit_index + 1
            if current_bit_index >= bits_length:
                break;

        if n_bits_to_modify >= 2:
            if str_as_bin[current_bit_index] == '1':
                x = x | (1 << 2)
            else:
                x = x & ~(1 << 2)

            current_bit_index = current_bit_index + 1
            if current_bit_index >= bits_length:
                break;

        if n_bits_to_modify >= 3:
            if str_as_bin[current_bit_index] == '1':
                x = x | (1 << 3)
            else:
                x = x & ~(1 << 3)

            current_bit_index = current_bit_index + 1
            if current_bit_index >= bits_length:
                break;

        if n_bits_to_modify >= 4:
            if str_as_bin[current_bit_index] == '1':
                x = x | (1 << 4)
            else:
                x = x & ~(1 << 4)

            current_bit_index = current_bit_index + 1
            if current_bit_index >= bits_length:
                break;

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

if __name__ == "__main__":
    hide_message()