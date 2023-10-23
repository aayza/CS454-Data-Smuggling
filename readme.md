# Operating instructions

## Encoding a message into an image

1. Run the python file called `encoding_cli.py`
2. In the CLI, enter the string message you would like to encode using only ASCII characters, e.g. "CAT" :)
3. Select the number of least significant bits you want to encode (between 1 and 4), the default is 1
4. Select a 24-bit BMP image by typing in a number (32-bit is unsupported), there is a simple 16 pixel image called test.bmp at the very minimum
   * Only small images are supported, recommended maximum resolution of 160 * 160 pixels
5. Your message's length including the unique exit string sequence will be checked to see if it can fit in the image then be encoded
6. Take a look at your output image in the folder called `output_images`, the image will have an epoch timestamp (yours will be the latest) and a default name, e.g. `1696324526_output_test.bmp`

## Decoding the message

1. Run `finding_message.py`, this will go through each image in the output_images folder and look for hidden messages