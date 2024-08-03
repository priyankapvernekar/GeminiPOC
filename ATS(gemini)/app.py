from dotenv import load_dotenv
load_dotenv()
import io
import os
import base64
import streamlit as st
from PIL import Image
import pdf2image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_response(input,pdfcv,prompt):

    model=genai.GenerativeModel('gemnini-pro-vision')
    response=model.generate_content([input,pdfcv,prompt])
    return response.text

def input_setup(pdf_file):
    ###convert the pdf to image
    if pdf_file is not None:
        image=pdf2image.convert_from_bytes(pdf_file.read())
        page1=image[0]

            #convert to bytes
        image_bytes_array=io.BytesIO()
        page1.save(image_bytes_array,format='JPEG')
        image_bytes_array=image_bytes_array.getvalue()

        pdf_parts=[
                {
                    "mime_type":"image/jpeg",
                    "data": base64.b4encode(image_bytes_array).decode
                }
            ]
        return pdf_parts
    else:
      raise FileNotFoundError("Please upload the CV")


## streamlit code

st.set_page_config(page_title="ATS expert")
st.header("ATS ")
input_text = st.text_area("Job Description ",key="input")
upload_file=st.file_uploader("choose your resume....",type=["PDF"])

if upload_file is not None:
    st.write("CV uploaded")

resumesubmit=st.button("brief about the resume")

skill= st.button(" skills required to be updated")

keyword =st.button("list all keyword missing")

matchpercent= st.button("percentage of match ")


input_promptbrief="""
you are the experienced HR with many tech knowledge like DataScience , full stack web developmemt and many more like data analyst etc 
your role is to """

input_prompt1 = """
 You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
  Please share your professional evaluation on whether the candidate's profile aligns with the role. 
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt3 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""

if resumesubmit:
    if upload_file is not None:
        pdf_content=input_setup(upload_file)
        response=get_response(input_prompt1,pdf_content,input_text)
        st.subheader("the brief explaination about CV")
        st.write(response)
    else:
        st.write(" upload the CV/resume")

elif matchpercent:
    if upload_file is not None:
        pdf_content=input_setup(upload_file)
        response=get_response(input_prompt3,pdf_content,input_text)
        st.subheader("the brief explaination about CV")
        st.write(response)
    else:
        st.write(" upload the CV/resume")