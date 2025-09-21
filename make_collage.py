from PIL import Image
import os

def create_collage(input_folder, output_file):
    images = []
    for file in os.listdir(input_folder):
        if file.endswith(".png"):
            images.append(Image.open(os.path.join(input_folder, file)))

    if not images:
        return None

    widths, heights = zip(*(i.size for i in images))
    total_width = sum(widths)
    max_height = max(heights)

    collage = Image.new("RGB", (total_width, max_height), (255, 215, 0))  # golden background
    x_offset = 0
    for im in images:
        collage.paste(im, (x_offset, 0))
        x_offset += im.size[0]

    collage.save(output_file)
    return output_file
