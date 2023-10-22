# Operating instructions

## Encoding a message into an image

1. Run the python file called `simple_encoding_cli.py`
2. In the CLI, enter a string message payload using only ASCII characters, it's best to keep this simple for the exercise
3. Select a 24-bit BMP image by typing in a number (32-bit is unsupported), there is a simple 16 pixel image called test.bmp for testing pursposes and also a cat_image2.bmp
4. Your message will then be encoded and the resulting message will pop up
5Retrieve your output image in the folder called `output_images`, the image will have an epoch timestamp and a default name, e.g. `1696324526_output_test.bmp`

## Decoding the message

1. Simply run `finding_message.py`, this will go through each image in the output_images folder and look for hidden messages