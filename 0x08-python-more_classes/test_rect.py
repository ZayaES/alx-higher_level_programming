#!/usr/bin/python3

Rectangle = __import__('1-rectangle').Rectangle

# Create a rectangle with default values
r1 = Rectangle()
print("Rectangle 1 - width:", r1.width, "height:", r1.height)

# Create a rectangle with specified values
r2 = Rectangle(10, 20)
print("Rectangle 2 - width:", r2.width, "height:", r2.height)

# Try to set width to a negative value
try:
    r2.width = -10
except ValueError as e:
    print("Error setting width:", e)

# Try to set width to a non-integer value
try:
    r2.width = 10.5
except TypeError as e:
    print("Error setting width:", e)

# Try to set width to None
try:
    r2.width = None
except TypeError as e:
    print("Error setting width:", e)

# Try to set height to None
try:
    r2.height = None
except TypeError as e:
    print("Error setting height:", e)

# Set width to a valid value
r2.width = 15
print("Rectangle 2 - width:", r2.width, "height:", r2.height)

# Try to set height to a negative value
try:
    r2.height = -20
except ValueError as e:
    print("Error setting height:", e)

# Try to set height to a non-integer value
try:
    r2.height = 20.5
except TypeError as e:
    print("Error setting height:", e)

# Set height to a valid value
r2.height = 25
print("Rectangle 2 - width:", r2.width, "height:", r2.height)
