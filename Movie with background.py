from PIL import Image
import os


def resize_images_in_directory(directory, size):
    for img_name in os.listdir(directory):
        if img_name.endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(directory, img_name)
            with Image.open(img_path) as img:
                img = img.resize(size, Image.ANTIALIAS)
                img.save(img_path)
            print(f"Resized and saved image: {img_name}")


def main():
    # Prompt user for directory and desired size
    images_dir = input("Enter the path to the directory containing images: ")
    width = int(input("Enter the width for resizing: "))
    height = int(input("Enter the height for resizing: "))

    # Check if the images directory exists
    if not os.path.exists(images_dir):
        print(f"The directory {images_dir} does not exist.")
        return

    # Resize images
    resize_images_in_directory(images_dir, (width, height))
    print("All images have been resized.")


if __name__ == "__main__":
    main()
