import os
from hiding_message import hide_message
from string_operations import string_to_binary

folder_path = "input_images"


def encode_message():
    # Step 1 Enter a string message (don't go nuts, keep it simple)

    while True:
        user_input = input("Type in the string message you want to encode:\n>")
        if user_input.strip():
            break
        else:
            print("Try again.")

    # Step 2 Select the number of bits to modify per byte
    while True:
        try:
            n_bits_to_modify = int(input("Please type in a number between 1 and 4 inclusive for the number of bits you wish to modify per byte:\n>"))
            if 1 <= n_bits_to_modify <= 4:
                break
            else:
                print("Invalid input. Please enter a number between 1 and 4 inclusive.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Step 3 Select an image to hide your message in
    bmp_image_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(".bmp")]

    if not bmp_image_files:
        print(f"No BMP image files found in the {folder_path} folder. Please add one to encode your message")
        return
    else:
        for i, image in enumerate(bmp_image_files, start=1):
            print(f"{i}. {image}")

    while True:
        try:
            choice = int(input("Enter the number of the BMP image you want to select (or 0 to exit):\n> "))
            if choice == 0:
                return
            elif 1 <= choice <= len(bmp_image_files):
                selected_image = bmp_image_files[choice - 1]

                # Step 4 Hide the message
                hide_message(user_input, selected_image, n_bits_to_modify)
                break
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


encode_message()
