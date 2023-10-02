from PIL import Image

def extract_bmp_channels_into_binary(filename = "input_images/test.bmp"):
    red_channel = []
    green_channel = []
    blue_channel = []

    try:
        with Image.open(filename) as img:
            header = img.info
            width, height = img.size
            # iterating through from top row and across
            for y in range(height):
                red_row = []
                green_row = []
                blue_row = []

                for x in range(width):
                    r, g, b = img.getpixel((x, y))

                    # 8-bit binary representation
                    r_binary = format(r, '08b')
                    g_binary = format(g, '08b')
                    b_binary = format(b, '08b')

                    red_row.append(r_binary)
                    green_row.append(g_binary)
                    blue_row.append(b_binary)

                red_channel.append(red_row)
                green_channel.append(green_row)
                blue_channel.append(blue_row)

            return header, img.size, red_channel, green_channel, blue_channel
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    header_info, img_size, red_channel, green_channel, blue_channel = extract_bmp_channels_into_binary()

    print("Header", header_info)
    print("Image size", img_size)
    print("Red channel  ", red_channel)
    print("Green channel", green_channel)
    print("Blue channel ", blue_channel)