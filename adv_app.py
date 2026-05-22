import streamlit as st
import pickle
import numpy as np
model = pickle.load(open('lr.sav','rb'))
st.title('Sales Prediction App')
#Input features
TV=st.number_input('TV adv budget', min_value=0.0)
Radio=st.number_input('Radio adv budget', min_value=0.0)
Newspaper=st.number_input('Newspaper adv budget', min_value=0.0)
if st.button('predict sales'):
  input_data=np.array([[TV,Radio,Newspaper]])
  Predction=model.predict(input_data)[0]
  st.success(f'Predicted sales: {Prediction:.2f}')
