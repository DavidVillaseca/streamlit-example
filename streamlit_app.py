import streamlit as st
from streamlit_image_comparison import image_comparison
import cv2


st.set_page_config("Deep Lung OP", "🦴☠")


st.image(
    "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/160/apple/325/lungs_1fac1.png",
    width=120,
)

st.header("Opacidad pulmonar y su mascara")

st.write("")
"Esta es una comparación entre un pulmon sano y uno opaco"
st.write("")

st.markdown("Paciente x")
image_comparison(
    img1="https://www.webbcompare.com/img/hubble/southern_nebula_700.jpg",
    img2="https://www.webbcompare.com/img/webb/southern_nebula_700.jpg",
    label1="Radiografía",
    label2="Máscara",
)

