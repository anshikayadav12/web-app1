import streamlit as st
from PIL import Image,ImageFilter
import os

#create a folder image
if not os.path.exists('images'):
    os.makedirs('images')

def save_images(image):
    img = Image.open(image)
    img.save(f'images/{image.name}.png')

st.title('Image Processing App')

upload = st.file_uploader(
    label='Upload your image',
    type=['png','jpg','jpeg']
)
if upload is not None:
    save_images(upload)
    st.image(
        upload,
        caption='Uploaded Image',
        use_column_width=True)
    
    filters=['contour','']