import time
import os

def read_file(file_name):
    current_folder = os.path.dirname(__file__)
    file_path = os.path.join(current_folder, file_name)

    with open(file_path, "r") as file:
        sentences = file.readlines()

    return sentences


def countdown():
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)

    print("Go!\n")