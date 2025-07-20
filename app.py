import streamlit as st
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageEnhance, ImageFilter

st.title("Images Management with Effects & Overlay")

# Sidebar: Upload images
uploaded_files = st.sidebar.file_uploader(
    "Upload Images", type=['png', 'jpg', 'jpeg'], accept_multiple_files=True)

# Sidebar controls for image effects
resize_factor = st.sidebar.slider("Resize (%)", 30, 100, 70)
rotate_angle = st.sidebar.slider("Rotate (degrees)", 0, 360, 0)
flip_horizontal = st.sidebar.checkbox("Flip Horizontal")
flip_vertical = st.sidebar.checkbox("Flip Vertical")
brightness = st.sidebar.slider("Brightness", 0.1, 3.0, 1.0)
contrast = st.sidebar.slider("Contrast", 0.1, 3.0, 1.0)
blur_radius = st.sidebar.slider("Blur Radius", 0, 10, 0)

# Overlay controls
overlay_text = st.sidebar.text_input("Overlay Text")
overlay_text_size = st.sidebar.slider("Overlay Text Size", 10, 100, 40)
overlay_text_color = st.sidebar.color_picker("Overlay Text Color", "#FFFFFF")

# Optional overlay image upload
overlay_img_file = st.sidebar.file_uploader(
    "Overlay Image (optional)", type=['png', 'jpg', 'jpeg'])

def process_image(image: Image.Image) -> Image.Image:
    # Resize
    new_w = int(image.width * resize_factor / 100)
    new_h = int(image.height * resize_factor / 100)
    image = image.resize((new_w, new_h), Image.LANCZOS)

    # Rotate
    image = image.rotate(rotate_angle, expand=True)

    # Flip
    if flip_horizontal:
        image = ImageOps.mirror(image)
    if flip_vertical:
        image = ImageOps.flip(image)

    # Adjust brightness and contrast
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(brightness)
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(contrast)

    # Blur
    if blur_radius > 0:
        image = image.filter(ImageFilter.GaussianBlur(blur_radius))

    # Overlay text
    draw = ImageDraw.Draw(image)
    try:
        font = ImageFont.truetype("arial.ttf", overlay_text_size)
    except:
        font = ImageFont.load_default()

    if overlay_text:
        bbox = draw.textbbox((0, 0), overlay_text, font=font)
        text_w = bbox[2] - bbox[0]
        text_h = bbox[3] - bbox[1]
        x = (image.width - text_w) // 2
        y = image.height - text_h - 10
        draw.text((x, y), overlay_text, font=font, fill=overlay_text_color)

    # Overlay image if uploaded
    if overlay_img_file:
        overlay_img = Image.open(overlay_img_file).convert("RGBA")
        ov_w = max(new_w // 4, 50)
        ov_h = int(overlay_img.height * (ov_w / overlay_img.width))
        overlay_img = overlay_img.resize((ov_w, ov_h), Image.LANCZOS)
        image.paste(
            overlay_img,
            ((image.width - overlay_img.width) // 2, (image.height - overlay_img.height) // 2),
            overlay_img
        )

    return image

if uploaded_files:
    st.write("### Uploaded Images Gallery:")

    cols = st.columns(2)  # 2 images per row

    for idx, uploaded_file in enumerate(uploaded_files):
        img = Image.open(uploaded_file).convert("RGBA")
        processed_img = process_image(img)

        with cols[idx % 2]:
            st.image(processed_img, use_column_width=True)
else:
    st.write("Upload images from the sidebar to see them here.")
