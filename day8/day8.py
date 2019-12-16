#!/usr/bin/python3

from collections import defaultdict

width = 25
height = 6
layer_size = width * height

def layers():
    with open("input", "r") as f:
        while True:
            layer_str = f.read(layer_size)
            if layer_str == "\n":
                break
            layer = list(map(int, layer_str))
            yield layer

def display_image(image):
    for x in range(height):
        line_start = x * width
        line_end = line_start + width
        line = "".join(map(lambda x: "#" if x == 1 else " ", final_image[line_start:line_end]))
        print(line)

if __name__ == "__main__":
    fewest_zeros = layer_size
    result = None
    final_image = [2 for x in range(layer_size)] # all transparent at the beginning
    for layer in layers():
        quantity = defaultdict(int)
        for i in range(layer_size):
            pixel = layer[i]
            quantity[pixel] += 1
            if final_image[i] == 2 and pixel != 2:
                final_image[i] = pixel
        if quantity[0] < fewest_zeros:
            fewest_zeros = quantity[0]
            result = quantity[1] * quantity[2]

    print(f"Task 1 result: {result}")
    display_image(final_image)
