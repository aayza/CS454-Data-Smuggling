# import needed functions
from finding_message import find_message
from hiding_message import hide_message

# define image to encode
image_path = "../input_images/cat.bmp"


def test_e2e(payload, least_sig_bit):
    payload_image = hide_message(payload, image_path, least_sig_bit)
    found_payload = find_message(payload_image)
    print(f"Original Payload: {payload}")
    print(f"Found Payload: {found_payload}")
    if payload == found_payload:
        return True
    return False


# e2e test for
if __name__ == '__main__':
    print('Running e2e tests... (this may take a few seconds)\n')
    for i in range(1, 5):
        if test_e2e('Test Cat', i):
            print(f"Success! correct payload extracted for {i} significant bit")
        else:
            print(f"Failure! extracting message for {i} significant bit")
        print('\n')
