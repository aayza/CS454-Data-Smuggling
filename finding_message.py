import os

from consts import EXIT_STRING
from image_operations import extract_bmp_pixels_as_rgb_bin
from string_operations import binary_to_string, binary_to_byte_array, binary_string_to_string


# Finds the encoded message within file provided as param.
# This supports any message that is encoded using either 1 2 3 or 4 least significant bit algorithm.
def find_message(file):
    if file is None or not os.path.isfile(file):
        error_message = "File not found. Could not decode message"
        print(error_message)
        return False

    # Extract file information for decoding
    header_info, img_size, rgb_binary = extract_bmp_pixels_as_rgb_bin(file)

    # Stores 4 potential encoded messages for each level of encoding (1-4 least sig bits)
    potential_messages = ['', '', '', '']

    for row in rgb_binary:
        for pixel in row:
            for byte in pixel:
                first_least_sig_bit = byte[7]
                second_least_sig_bit = byte[6]
                third_least_sig_bit = byte[5]
                forth_least_sig_bit = byte[4]
                if first_least_sig_bit is not None:
                    # Decode for least significant bit
                    potential_messages[0] += first_least_sig_bit

                    # Decode for least 2 significant bits
                    potential_messages[1] += first_least_sig_bit
                    potential_messages[1] += second_least_sig_bit

                    # Decode for least 3 significant bits
                    potential_messages[2] += first_least_sig_bit
                    potential_messages[2] += second_least_sig_bit
                    potential_messages[2] += third_least_sig_bit

                    # Decode for least 4 significant bits
                    potential_messages[3] += first_least_sig_bit
                    potential_messages[3] += second_least_sig_bit
                    potential_messages[3] += third_least_sig_bit
                    potential_messages[3] += forth_least_sig_bit

    # Finds the message within potential_messages that includes EXIT_STRING
    for message in potential_messages:
        # Get message as bytes
        message_bytes = binary_to_byte_array(message)
        # Get message as string
        message_string = binary_string_to_string(message_bytes)
        # Check message contains exit string - meaning it is the message we are looking for
        if EXIT_STRING in message_string:
            found_message = message_string.split(EXIT_STRING)[0]
            return found_message

    # If no potential_messages contain the exit string
    # No message exists or was encoded using a different algorithm or combination of least sig bits
    print("message not found. ")


# Decode all files inside output_images
if __name__ == "__main__":
    directory = "output_images"
    images_to_decode = os.listdir(directory)

    if len(images_to_decode) == 0:
        print("No images to decode.")
    else:
        for filename in os.listdir(directory):
            path = directory + "/" + filename
            f = os.path.join(directory, filename)
            print(filename, "Message:", find_message(f))
