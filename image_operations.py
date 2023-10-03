from PIL import Image


default_filename = "input_images/test.bmp"

def extract_bmp_channels_ints(filename = default_filename):
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

                    red_row.append(r)
                    green_row.append(g)
                    blue_row.append(b)

                red_channel.append(red_row)
                green_channel.append(green_row)
                blue_channel.append(blue_row)

            return header, img.size, red_channel, green_channel, blue_channel
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    header_info, img_size, red_channel, green_channel, blue_channel = extract_bmp_channels_ints()

    print("Header", header_info)
    print("Image size", img_size)
    print("Red channel  ", red_channel)
    print("Green channel", green_channel)
    print("Blue channel ", blue_channel)

    # As binary strings
    red_as_binary = [[bin(num)[2:] for num in sublistrow] for sublistrow in red_channel]
    green_as_binary = [[bin(num)[2:] for num in sublistrow] for sublistrow in green_channel]
    blue_as_binary = [[bin(num)[2:] for num in sublistrow] for sublistrow in green_channel]
    print("Red", red_as_binary)
    print("Green", green_as_binary)
    print("Blue", blue_as_binary)