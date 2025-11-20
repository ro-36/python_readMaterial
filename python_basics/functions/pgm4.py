import math

def circle(r):
    area = math.pi * r ** 2
    circumference = 2* math.pi * r

    return area, circumference

area, circumference = circle(5)
print(f"Area: {area}, Circumference: {circumference}")