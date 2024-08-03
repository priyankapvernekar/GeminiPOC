from dotenv import load_dotenv

load_dotenv()

import streamlit as st # for interface

import os  # picking env variable

from PIL import Image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#using gemini pro vision for this use case as the input will be image

model=genai.GenerativeModel('gemini-pro-vision')

def get_response(input,image,prompt):
    response=model.generate_content([input,image[0],prompt])
    return response.text
    #input what is assistant want to do example saying the role that LLI shouuld perform 
    #image is the invoice image
    #prompt are the question that you/user will ask related to given image
st.set_page_config(page_title='INVOICE EXTRACTER')
  
st.header("APP")
input=st.text_input("Your question ",key="input")
upload_file=st.file_uploader('choose an image  ', type=["jpg","jpeg","png"]) 
image=""
if upload_file is not None:
    image=Image.open(upload_file)
    st.image(image,caption="Uploaded Image" , use_column_width=True)

submit=st.button("information about the invoice")

input_prompt="""YOU are an expert in understanding invoices .we will upload a image as invoice and you will
have to answer any question asked related to given invoice """

def input_image(upload_file):
    if upload_file is not None:
        bytes_data =upload_file.getvalue()
        image_parts =[
            {
                "mime_type":upload_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
if submit:
    image_data=input_image(upload_file)
    response=get_response(input_prompt,image_data,input)
    st.subheader("here is your answer")
    st.write(response)