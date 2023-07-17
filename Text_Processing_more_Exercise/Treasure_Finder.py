import re

nums = [int(x) for x in input().split()]

while True:
    text = input()

    if text == "find":
        break

    index = 0
    message = ""

    for el in text:
        new_ord = ord(el) - nums[index]
        message += chr(new_ord)
        index += 1
        if index == len(nums):
            index = 0

    regex_type = r"(?<=&)[A-Za-z]+(?=&)"
    regex_coordinates = r"(?<=<)[A-Za-z0-9]+(?=>)"

    type_ = re.findall(regex_type, message)
    coordinates = re.findall(regex_coordinates, message)

    print(f"Found {type_[0]} at {coordinates[0]}")



