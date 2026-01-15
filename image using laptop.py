import streamlit as st
from PIL import Image

st.title("Camera Image Processing")

img = st.camera_input("Take a picture")

if img:
    image = Image.open(img)
    gray = image.convert("L")

    st.image(image, caption="Original Image")
    st.image(gray, caption="Grayscale Image")
