import io
import streamlit as st

from PIL import Image
from cnocr import CnOcr


def load_image():
    uploaded_file = st.file_uploader(label='Выберите изображение для распознавания')
    if uploaded_file is not None:
        image_data = uploaded_file.getvalue()
        st.image(image_data)
        return Image.open(io.BytesIO(image_data))
    else:
        return None


st.title('🎈 Распознование китайского языка с изображения')
img = load_image()

result = st.button('Распознать изображение')

if result:
    text = CnOcr().ocr(img)
    st.write('**Результаты распознавания:**')
    st.write("\n\n".join(i["text"] for i in text))
    # Объединяет распознанные текстовые фрагменты в одну строку с разделением по строкам (через \n)
