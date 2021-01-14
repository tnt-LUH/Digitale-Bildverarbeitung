import os
import numpy as np
import cv2


def check_result(image) -> bool:
    """
    Loads the checksum and compares it to the checksum of the result
    :param image:
    :return:
    """
    # Load checksum
    directory = os.path.dirname(__file__)
    checksum_file = os.path.join(directory, "checksum")
    assert os.path.isfile(checksum_file), "Checksum file %s is not existing" % checksum_file
    f = open(checksum_file, "r")
    result_image_hash = f.read()
    f.close()
    # Compare hashes
    new_image_hash = str(hash(str(image)+str(image.shape)))
    if result_image_hash == new_image_hash:
        print('\033[92m' + "Your solution for excercise %s is CORRECT!" % directory + '\033[0m')
        return True
    else:
        print('\033[91m' + "Your solution for excercise %s is INCORRECT!" % directory + '\033[0m')
        return False


def store_checksum(image):
    """
    Loads the checksum and compares it to the checksum of the result
    :param image:
    :return:
    """
    # Load checksum
    directory = os.path.dirname(__file__)
    checksum_file = os.path.join(directory, "checksum")
    image_hash = str(hash(str(image)+str(image.shape)))
    f = open(checksum_file, "w+")
    f.write(image_hash)
    f.close()


''' The following code is for testing and development purposes '''
if __name__ == "__main__":
    store_checksum(np.ones((100, 100, 3)))
    check_result(np.ones((100, 100, 3)))