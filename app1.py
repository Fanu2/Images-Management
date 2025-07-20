import streamlit as st
from PIL import Image, ImageEnhance
import os
from io import BytesIO

st.set_page_config(page_title="Image Manager", layout="wide")
st.title("🖼️ Image Manager")

# Directory to store processed images
SAVE_DIR = "saved_images"
os.makedirs(SAVE_DIR, exist_ok=True)

uploaded_files = st.file_uploader("Upload images", type=["png", "jpg", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    format_options = ["JPEG", "PNG", "WEBP"]
    st.sidebar.header("🛠️ Processing Options")
    output_format = st.sidebar.selectbox("Convert to Format", format_options)

    # Resize options
    resize = st.sidebar.checkbox("Resize Images")
    width = height = None
    if resize:
        width = st.sidebar.number_input("Width (px)", min_value=1, value=512)
        height = st.sidebar.number_input("Height (px)", min_value=1, value=512)

    # Additional effects
    st.sidebar.header("🎨 Image Effects")
    rotate_angle = st.sidebar.slider("Rotate (degrees)", -180, 180, 0)
    to_gray = st.sidebar.checkbox("Convert to Grayscale")
    enhance_contrast = st.sidebar.slider("Contrast", 0.5, 3.0, 1.0, 0.1)
    enhance_sharpness = st.sidebar.slider("Sharpness", 0.5, 3.0, 1.0, 0.1)
    enhance_brightness = st.sidebar.slider("Brightness", 0.5, 3.0, 1.0, 0.1)

    st.subheader("📂 Preview & Processed Images")
    cols = st.columns(3)

    for i, uploaded_file in enumerate(uploaded_files):
        img = Image.open(uploaded_file)

        # Apply resizing
        if resize and width and height:
            img = img.resize((width, height))

        # Apply effects
        if rotate_angle != 0:
            img = img.rotate(rotate_angle)
        if to_gray:
            img = img.convert("L")
        else:
            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(enhance_contrast)
            enhancer = ImageEnhance.Sharpness(img)
            img = enhancer.enhance(enhance_sharpness)
            enhancer = ImageEnhance.Brightness(img)
            img = enhancer.enhance(enhance_brightness)

        # Save processed image
        base_filename = os.path.splitext(uploaded_file.name)[0]
        out_filename = f"{base_filename}_edited.{output_format.lower()}"
        out_path = os.path.join(SAVE_DIR, out_filename)
        img.save(out_path, format=output_format)

        # Show in column
        with cols[i % 3]:
            st.image(img, caption=out_filename, use_column_width=True)
            with open(out_path, "rb") as f:
                st.download_button(
                    label="📥 Download",
                    data=f,
                    file_name=out_filename,
                    mime=f"image/{output_format.lower()}",
                )

    st.success(f"🎉 Processed {len(uploaded_files)} image(s) saved to `{SAVE_DIR}/`")
