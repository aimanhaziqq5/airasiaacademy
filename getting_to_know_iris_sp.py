import streamlit as st
import pandas as pd
import seaborn as sns
from sklearn.naive_bayes import GaussianNB
import pickle

st.write("# Iris Species Prediction")
st.write("This app predicts the **Iris flower** species!")

st.sidebar.header('Score the following characteristics')

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal Length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal Width', 2.0, 4.4, 3.1)
    petal_length = st.sidebar.slider('Petal Length', 1.0, 6.9, 3.9)
    petal_width = st.sidebar.slider('Petal Width', 0.1, 2.5, 1.5)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('Insert Parameters')
st.write(df)

loaded_model = pickle.load(open("IrisPrediction2.h5", "rb"))
prediction = modelIrisClass.predict(df)
prediction_proba = modelIrisClass.predict_proba(df)

st.subheader('Species categories and their corresponding index number')
st.write(Y.unique())

st.subheader('Prediction')
st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)
