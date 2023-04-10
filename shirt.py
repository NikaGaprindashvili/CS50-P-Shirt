import sys
import os
from PIL import Image, ImageOps

# Check if the number of arguments is correct
if len(sys.argv) != 3:
    sys.exit("Usage: python shirt.py input_image output_image")

# Check if the input and output files have valid extensions
valid_extensions = ('.jpg', '.jpeg', '.png')
input_ext = os.path.splitext(sys.argv[1])[1].lower()
output_ext = os.path.splitext(sys.argv[2])[1].lower()
if not (input_ext in valid_extensions and output_ext in valid_extensions):
    sys.exit("Error: input and output files must have .jpg, .jpeg, or .png extension")

# Check if the input and output files have the same extension
if input_ext != output_ext:
    sys.exit("Error: input and output files must have the same extension")

# Check if the input file exists
if not os.path.exists(sys.argv[1]):
    sys.exit("Error: input file does not exist")

# Open the input image
input_image = Image.open(sys.argv[1])

# Resize and crop the input image to match the size of shirt.png
shirt_size = Image.open("shirt.png").size
input_image = ImageOps.fit(input_image, shirt_size)

# Overlay shirt.png on the input image
shirt = Image.open("shirt.png")
input_image.paste(shirt, shirt)

# Save the result as the output file
input_image.save(sys.argv[2])
