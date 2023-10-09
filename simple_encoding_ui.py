import os
from hiding_message import hide_message
from string_operations import string_to_binary

folder_path = "input_images"

def encode_message():
    user_input = input("Type in a string message.")
    print(f"Your message is {user_input}")

    while True:
        try:
            n_bits_to_modify = int(input("Please type in a number between 1 and 4 inclusive for the number of bits you wish to modify per byte: "))
            if 1 <= n_bits_to_modify <= 4:
                break
            else:
                print("Invalid input. Please enter a number between 1 and 4 inclusive.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"You typed the number: {n_bits_to_modify}")

    bmp_image_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(".bmp")]

    if not bmp_image_files:
        print(f"No BMP image files found in the {folder_path} folder.")
    else:
        print(f"Choose a BMP image in the {folder_path} folder:")
        for i, image in enumerate(bmp_image_files, start=1):
            print(f"{i}. {image}")

    while True:
        try:
            choice = int(input("Enter the number of the BMP image you want to select (or 0 to exit): "))
            if choice == 0:
                break
            elif 1 <= choice <= len(bmp_image_files):
                selected_image = bmp_image_files[choice - 1]
                print(f"You selected: {selected_image}")

                string_binary = string_to_binary(user_input)
                hide_message(string_binary, selected_image, n_bits_to_modify)
                break
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

encode_message()