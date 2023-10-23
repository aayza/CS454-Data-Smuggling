# import needed functions
from finding_message import find_message
from hiding_message import hide_message
from string_operations import string_to_binary, binary_string_to_string

# TODO Should i have this hardcoded or a cli?

# define secret message
message = "test message"

# define image to encodehas
image_path = "input_images/cat_image4.bmp"

# define bits to modify
bits_to_modify = 4


# convert the message into binary and then encode the secret message into the provided image using imported functions
def encode(input_string, image_file, n_bits_to_modify):
    # string_binary = string_to_binary(input_string)
    payload_image = hide_message(input_string, image_file, n_bits_to_modify)
    return payload_image


# decode the payload image with the imported function which finds the encoded message binary and then converts this back to a string
def decode(payload_image):
    finding_message = find_message(payload_image)
    # decoded_message = binary_string_to_string(finding_message)
    return finding_message


# verify that the original message passed through is the same as the decoded message
def verification(original_message, decoded_message):
    if original_message == decoded_message:
        return True
    else:
        return False


# Run all steps and provide user with a message
if __name__ == '__main__':
    encoded_image = encode(message, image_path, bits_to_modify)
    found_message = decode(encoded_image)
    if verification(message, found_message):
        user_message = "The encoding/decoding successfully worked! \n\nThe original message \"" + message + "\" was successfully hidden in the image \"" + image_path + " \" and created new image \"" + encoded_image + "\" which was then decoded to find the message \"" + found_message + "\"!"
    else:
        user_message = "The encoding/decoding did not work :("
    print(user_message)
