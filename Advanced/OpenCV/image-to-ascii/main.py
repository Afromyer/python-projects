import cv2 as cv

image_path = input("Give an image path: ")

img = cv.imread(image_path)

# Define the new width and height
new_width = 640
new_height = 480

# Resize the image
resized_image = cv.resize(img, (new_width, new_height), interpolation=cv.INTER_LINEAR)

img_list = resized_image.tolist()

for row in range(len(img_list)):
    for pixel in range(len(img_list[row])):
        average_value = round((img_list[row][pixel][0] + img_list[row][pixel][1] + img_list[row][pixel][2]) / 3)
        img_list[row][pixel] = average_value

print("Successfully constructed brightness matrix!")
print(f"Brightness matrix size: {len(img_list[0])} x {len(img_list)}")


def to_ascci(brightness_value):
    ASCII = r"`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    percentage = (brightness_value / 255) * 100
    ascii_index = int((percentage / 100) * len(ASCII) - 1)
    return ASCII[ascii_index]

print("Converting to Ascii...")

for row in range(len(img_list)):
    for pixel in range(len(img_list[row])):
        img_list[row][pixel] = to_ascci(img_list[row][pixel]) * 3
    print("".join(img_list[row]))
