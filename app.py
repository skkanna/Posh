# -*- coding: utf-8 -*-
"""
Created on Fri May 15 12:50:04 2020

@author: KamalaKannan Sampath
"""
#!pip3 install -U Flask
#from flask import Flask, request
import numpy as np
import pickle
import pandas as pd
import streamlit as st
from PIL import Image
#import flasgger
#from flasgger import Swagger

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("regressor.pkl","rb")
regressor=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def price_pred(attr1_2, attr1_3, attr1_4, attr2,
                                      attr3, attr4, attr5_2, attr5_3, attr6):
    
    
    """Let's look at the number of orders 
    This is using docstrings for specifications.
    ---
    parameters:
                  
      - name: attr1_2.0
        in: query
        type: number
        required: true
      - name: attr1_3.0
        in: query
        type: number
        required: true
      - name: attr1_4.0
        in: query
        type: number
        required: true
      - name: attr2
        in: query
        type: number
        required: true
      - name: attr3
        in: query
        type: number
        required: true
      - name: attr4
        in: query
        type: number
        required: true
      - name: attr5_2
        in: query
        type: number
        required: true
      - name: attr5_3
        in: query
        type: number
        required: true
      - name: attr6
        in: query
        type: number
        required: true
     
      
    responses:
        200:
            description: The output values
        
    """
    prediction=regressor.predict([[attr1_2, attr1_3, attr1_4, attr2, 
                  attr3, attr4, attr5_2, attr5_3, 
                  attr6]])
    
    print(prediction)
    return prediction

#@app.route('/predict_file',methods=["Post"])
def main():
    st.title("Price Predictor")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Price Predictor ML App </h2>
    </div>
    """

    st.markdown(html_temp,unsafe_allow_html=True)    
    
    attr1_2 = st.number_input("attr1_2.0", value=1.)
    attr1_3 = st.number_input("attr1_3.0", value=1.)
    attr1_4 = st.number_input("attr1_4.0", value=1.)
    attr2 = st.number_input("attr2", value=1.)
    attr3 = st.number_input("attr3", value=1.)
    attr4 = st.number_input("attr4", value=1.)
    attr5_2 = st.number_input("attr5_2", value=1.)
    attr5_3 = st.number_input("attr5_3", value=1.)
    attr6 = st.number_input("attr6", value=1.)
    
        
    result=""
    if st.button("Predict"):
                    
        result=price_pred(attr1_2, attr1_3, attr1_4, attr2, 
                  attr3, attr4, attr5_2, attr5_3, 
                  attr6)
        
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets Learn")
        st.text("Built with Streamlit")  
    
if __name__=='__main__':
    main()