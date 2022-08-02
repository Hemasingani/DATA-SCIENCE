import streamlit as st
import numpy as np
from pickle import load
from PIL import Image


uploaded_file = st.file_uploader("Choose a file",type=["png","jpg"])

if uploaded_file is not None:
	img=Image.open(uploaded_file)
	c=img.convert('L')
	h=c.resize((28,28))

	e=np.array(h)
	d=e.flatten()

	d1=np.array(d)

	st.image(uploaded_file)

btn_click=st.button("predict")

if btn_click==True:
	
	model=load(open(r'C:\Users\dell\Desktop\MACHINE LEARNING PROJECTS\ml-handwritten-sprint1\Image data\logistic_regression.pkl','rb'))
#here i have taken logistic model for prediction bcz it is showing better predicted values:


	pred=model.predict(d1.reshape(1,-1))
	st.text("The Image is : ")
	st.title(pred[0])
 


#for logistic regression : 88% accuracy
#the images are giving better predictions:
#0-0
#1-8
#2-2
#5-5
#6-5
#8-8
#SO IT GIVING 4 POSSIBLE PREDICTED VALUES.
#OUR LOGISTIC REGRESSION MODEL IS  PERFORMING GOOD.

