import stremlit as st
import pickle
import numpy as np
model = pickle.load(open('lr.sav','rb'))
st.title('Sales Prediction App')
#Input features
TV=st.number_input('TV adv budget', min_value=0.0)
Radio=st.number_input('Radio adv budget', min_value=0.0)
Newspaper=st.number_input('Newspaper adv budget', min_value=0.0)
if st.button('predct sales'):
  input_data=np.array([[TV,Radio,Newspaper]])
  predction=model.predict(input_data)[0]
  st.success(f'predicted sales: {Prediction:.2f)')
