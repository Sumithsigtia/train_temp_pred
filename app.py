import streamlit as st
import pickle
import sklearn
import pandas as pd
import numpy as np
from PIL import Image

model = pickle.load(open('model.sav', 'rb'))

st.title('Railway Track Temperature Prediction')
st.header('Railway Track Temperature Data')
image = Image.open('train.jpg')
st.image(image, '')

# FUNCTION
def user_report():
    time = st.slider('Time (in seconds)', 0, 3600, 1)
    Frequency_Kmph = st.slider('Speed (in kmph)', 0, 100, 1)  # Set step size to 10
    Weight_Kg = st.slider('Weight (in Kgs)', 0, 500, 1)  # Set step size to 5

    user_report_data = {
        'time': time,
        'Frequency(Kmph)': Frequency_Kmph,
        'Weight(Kg)': Weight_Kg
    }
    report_data = pd.DataFrame(user_report_data, index=[0])
    return report_data

user_data = user_report()
st.header('Railway Track Temperature Data')
st.write(user_data)

temperature = model.predict(user_data)
st.subheader('Railway Track Temperature')
st.subheader(np.round(temperature[0], 2))
