from PIL import Image
import os


def compress_image(input_path, output_path, quality=85, max_size=(800, 800)):
    # open image
    with Image.open(input_path) as img:
        # Resize the image if it's larger than max_size
        img.thumbnail(max_size, Image.LANCZOS)

        # Save the image with the specified quality
        img.save(output_path, quality=quality, optimize=True)


# Example usage
input_image_path = ''  # give path to File and filename with extension
current_dir = os.getcwd()
output_image_path = f"{current_dir}/compressed_image.png"
# if you want change output file name and path.
# Right now the program path is current dir of program
compress_image(input_image_path, output_image_path, quality=70, max_size=(1300, 800))  # op File size
