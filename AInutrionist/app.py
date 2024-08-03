import os
from dotenv import load_dotenv
import google.generativeai as genai
import streamlit as st
from PIL import Image


load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_response(input_prompt,io_image):
    model=genai.GenerativeModel("gemini-pro-vision")
    response=model.generate_content([input_prompt,io_image[0]])
    return response.text

def image_setup(io_image):
    if io_image is not None:
        image_data=io_image.getvalue()
        image_parts=[{
            "mime_type":io_image.type,
            "data":image_data
        }]
        return image_parts
    else:
        raise FileNotFoundError("upload the food image")
    

st.set_page_config(page_title="FRIEND DIETION")
io_image=st.file_uploader("upload your food image",type=["jpg","jpeg","png"])
image=""
if io_image is not None:
    image=Image.open(io_image)
    st.image(image,caption="your food",use_column_width=True)

submit= st.button("total calories")

input_prompt="""
YOU are the expert nutritionist. You will be provided with the picture of food items , 
you have to recoginze the food and give the quantity of the food ;
example : consisder the plate contains indian bread , curry , salad
 output should be in tabular columns : with columns names food items quantity in grams  calories Protien Fiber Fat 
       indian bread : 300 gram   8 1 0.4
       curry : 250 gram
       salad :500 gram
       and last row will be sum 
AS nutritionist later you can suggest That plate is healthy or Not ,what can be the changes to make it healthy.
"""


if submit:
    image1=image_setup(io_image)
    response=get_response(input_prompt,image1)
    st.subheader("your calorie chart")
    st.write(response)


    
