import os
from reportlab.lib.pagesizes import portrait
from reportlab.pdfgen import canvas
from PIL import Image


def create_photo_album(images_folder, output_pdf):
    # List all image files in the folder
    image_files = [f for f in os.listdir(images_folder) if f.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

    # Create PDF canvas
    c = canvas.Canvas(output_pdf, pagesize=(1024, 1024))

    # Iterate through image files and add to PDF pages
    for image_file in image_files:
        image_path = os.path.join(images_folder, image_file)
        image = Image.open(image_path)

        # Resize image to fit within 1024x1024 page size
        image.thumbnail((1024, 1024), Image.ANTIALIAS)

        # Calculate positioning to center image on the page
        x = (1024 - image.width) / 2
        y = (1024 - image.height) / 2

        # Draw image on canvas
        c.drawImage(image_path, x, y, width=image.width, height=image.height)

        # Add a new page for the next image
        c.showPage()

    c.save()
    print(f"Photo album saved as PDF: {output_pdf}")


if __name__ == "__main__":
    images_folder = "/home/jasvir/Documents/Slide show/"  # Replace with your image folder path
    output_pdf = "/home/jasvir/Documents/photo_album.pdf"  # Output PDF file path

    create_photo_album(images_folder, output_pdf)
