import streamlit as st
from PIL import Image, ImageOps
import io

uploaded_file = st.file_uploader("Загрузить изображение", type=["jpg", "png", "jpeg"])

transformation = st.radio("Преобразование:", ["Изменение размера", "Конвертация в Чёрно-белое"])

if transformation == "Изменение размера":
    width = st.number_input("Ширина:", value=100)
    height = st.number_input("Высота:", value=100)

if st.button("Обработать"):
    if uploaded_file is not None:
        
        image = Image.open(uploaded_file)
        
        
        st.image(image, caption="Исходное изображение")
        
        
        if transformation == "Конвертация в Чёрно-белое":
            processed_image = ImageOps.grayscale(image)
        elif transformation == "Изменение размера":
            processed_image = image.resize((width, height))
        
        
        st.image(processed_image, caption="Обработанное изображение")
        
        
        processed_image_path = "C:/Users/Gulnaz/Downloads/image.png"
        processed_image.save(processed_image_path)
        
      
        with open(processed_image_path, "rb") as f:
            st.download_button(
                label="Скачать обработанное изображение",
                data=f,
                file_name="image.png",
                mime="image/png"
            )
        st.write("Изображение обработано и сохранено")
