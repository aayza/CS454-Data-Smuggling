def string_to_binary(input_string):
    output_array = []

    for char in input_string:
        binary_char = bin(ord(char))[2:] # Get the ASCII value of the character and convert it to binary with 'bin()'

        # Ensure that each binary representation is 8 bits long by adding leading zeros if needed
        while len(binary_char) < 8:
            binary_char = "0" + binary_char

        output_array.append(binary_char)

    return output_array

def binary_to_string(input_binary_string_list):
    result_str = ""

    # re-encode each string byte representation back to its character
    for letter_binary in input_binary_string_list:
        char_code = int(letter_binary, 2)
        result_str += chr(char_code)

    return result_str

if __name__ == '__main__':
    input_str = "Hello, World!"
    binary_str = string_to_binary(input_str)
    print(binary_str)
    print(binary_to_string(binary_str))


