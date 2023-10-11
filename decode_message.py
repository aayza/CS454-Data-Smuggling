import os

from consts import EXIT_STRING
from image_operations import extract_bmp_pixels_as_rgb_bin
from string_operations import binary_to_string


def decode_message(file):
    header_info, img_size, rgb_binary = extract_bmp_pixels_as_rgb_bin(file)

    message_binary = ''

    for row in rgb_binary:
        for pixel in row:
            for byte in pixel:
                least_sig_bit = byte[7]
                if least_sig_bit is not None:
                    message_binary += least_sig_bit

    # TODO - simplify this nonsense - helper function for bit array to groups of bytes
    message_binary = [message_binary[i:i + 8] for i in range(0, len(message_binary), 8)]
    message = binary_to_string(message_binary)
    message = message.split(EXIT_STRING)[0]
    print(message)


if __name__ == "__main__":
    directory = "output_images"
    images_to_decode = os.listdir(directory)

    if len(images_to_decode) == 0:
        print("No images to decode :(")
    else:
        for filename in os.listdir(directory):
            f = os.path.join(directory, filename)
            if os.path.isfile(f):
                decode_message(f)
