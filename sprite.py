# Python script to create a sprite sheet using labelled frame images

import os
from PIL import Image

# Initial Configurations------------------[BEGIN]

INPUT_FOLDER_PATH = 'Knob'
CROP_BOX = (872, 412, 1117, 647) # (left, top, right, bottom)
OUTPUT_SPRITE_SHEET_PATH = 'knob_sprite.png'

# Initial Configurations------------------[END]

image_files = []

for file in os.listdir(INPUT_FOLDER_PATH):
    if (file.lower().endswith('.png')):
        image_files.append(file)        

count = 0
images = []

# Cropping images
for image_file in image_files:
    img_path = os.path.join(INPUT_FOLDER_PATH, image_file)
    img = Image.open(img_path).convert("RGBA")

    # Crop Image
    img_cropped = img.crop(CROP_BOX)
    images.append(img_cropped)

    name_parts = os.path.splitext(image_file)

    # Save cropped image and delete original image
    img_cropped.save(os.path.join(INPUT_FOLDER_PATH, name_parts[0]+'_cropped'+name_parts[1]))
    os.remove(img_path)
    count += 1


# Frame and Sprite Sheet dimensions calculation
frame_width = CROP_BOX[2] - CROP_BOX[0]
frame_height = CROP_BOX[3] - CROP_BOX[1]

sheet_width = frame_width*count
sheet_height = frame_height

# Create blank sprite sheet
sprite_sheet = Image.new("RGBA",(sheet_width,sheet_height))

# Place frames on the sprite sheet
for index, image in enumerate(images):
    x = index*frame_width
    y = 0
    sprite_sheet.paste(image,(x,y))

# Save sprite sheet
sprite_sheet.save(OUTPUT_SPRITE_SHEET_PATH)
print(f"Output sprite sheet saved at {OUTPUT_SPRITE_SHEET_PATH}.")