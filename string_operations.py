# Input for this def should be a string, e.g. "ABC"
# Output will be list of ASCII characters in binary form, e.g. ["01000001","01000010","01000011"]
def string_to_binary(input_string):
    output_array = []

    for char in input_string:
        binary_char = bin(ord(char))[2:]  # Get the ASCII value of the character and convert it to binary with 'bin()'

        # Ensure that each binary representation is 8 bits long by adding leading zeros if needed
        while len(binary_char) < 8:
            binary_char = "0" + binary_char

        output_array.append(binary_char)

    return output_array


def binaryString_to_string(binary_string):
    binary_string = str(binary_string)
    # Remove any characters that are not '1' or '0'
    binary_string = ''.join(char for char in binary_string if char in '01')

    # Split the binary string into 8-bit chunks
    binary_chunks = [binary_string[i:i + 8] for i in range(0, len(binary_string), 8)]

    # Convert each 8-bit binary chunk to its decimal representation and then to a character
    text_characters = [chr(int(chunk, 2)) for chunk in binary_chunks]

    # Join the characters to form the resulting string
    result_string = ''.join(text_characters)

    return result_string


# Input for this def should be a list of ASCII characters in binary form, e.g. ["01000001","01000010","01000011"]
# Output will be a normal string, e.g. "ABC"
def binary_to_string(input_binary_string_list):
    result_str = ""

    # re-encode each string byte representation back to its character
    for letter_binary in input_binary_string_list:
        char_code = int(letter_binary, 2)
        result_str += chr(char_code)

    return result_str


# Input for this def should be a string, e.g. "ABC"
# Output will be list of ASCII characters in ints, e.g. [65, 66, 67]
def string_to_char_ints(input_string):
    output = []
    for c in input_string:
        output.append(ord(c))
    return output


# Input is e.g. [72, 101, 108, 108, 111]
# Output is "Hello"
def ints_list_to_str(input_int_list):
    char_list = [chr(int_value) for int_value in input_int_list]
    resulting_string = ''.join(char_list)
    return resulting_string


# Input is a binary string e.g. "010000010010101010101010101010101010..."
# Output is ["01000001","01000010","01000011"]
def binary_to_byte_array(binary):
    return [binary[i:i + 8] for i in range(0, len(binary), 8)]


# Test main
if __name__ == '__main__':
    input_str = "Hello, World!"
    binary_str = string_to_binary(input_str)
    print(binary_str)
    print(binary_to_string(binary_str))

    print(string_to_char_ints("ABC"))
    print(ints_list_to_str([65, 66, 67]))
