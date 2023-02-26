import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "pic.jpg")
img = image.imread(IMAGE_PATH)

st.title('Sanjay Kumar Pudari')
st.header('**:blue[Data Science Intern:sunglasses:]**')
st.subheader(":red[Innomatics Research labs]")

btn_click = st.button("To know more details about me...click here")
if btn_click == True:
    st.subheader("wow! I'm glad that.. you wanna know about me :heart_eyes:")
    st.caption('**I am a recent master graduate and data enthusiastic who loves to explore data and do statistical problems and interested in Data Science**')
    
    st.subheader('this is me...:stuck_out_tongue:')
    st.image(img,width=120)

    st.markdown('**Linkedin : www.linkedin.com/in/sanjay-kumar-318464210**')
    st.markdown('**GitHub: https://github.com/SanjayKumarPudari**')
