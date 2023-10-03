# Input for this def should be a string, e.g. "ABC"
# Output will be list of ASCII characters in binary form, e.g. ["01000001","01000010","01000011"]
def string_to_binary(input_string):
    output_array = []

    for char in input_string:
        binary_char = bin(ord(char))[2:] # Get the ASCII value of the character and convert it to binary with 'bin()'

        # Ensure that each binary representation is 8 bits long by adding leading zeros if needed
        while len(binary_char) < 8:
            binary_char = "0" + binary_char

        output_array.append(binary_char)

    return output_array

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


def ints_list_to_str(input_int_list):
    char_list = [chr(int_value) for int_value in input_int_list]
    resulting_string = ''.join(char_list)
    return resulting_string


if __name__ == '__main__':
    input_str = "Hello, World!"
    binary_str = string_to_binary(input_str)
    print(binary_str)
    print(binary_to_string(binary_str))

    print(string_to_char_ints("ABC"))
    print(ints_list_to_str([65,66,67]))


