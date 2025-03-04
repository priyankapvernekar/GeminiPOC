import streamlit as st
import os
import google.generativeai as genai
import PyPDF2 as pdf

from dotenv import load_dotenv

load_dotenv()


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_response(input):
    model=genai.GenerativeModel("gemini-pro")
    response=model.generate_content(input)
    return response.text

def get_text(pdffile):
    document=pdf.PdfReader(pdffile)
    text=""
    for page in range(len(document.pages)):
        page=document.pages[page]
        text+=str(page.extract_text())
    return text


input_prompt="""
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving thr resumes. Assign the percentage Matching based 
on Jd and
the missing keywords with high accuracy
resume:{text}
description:{jd}

I want the response in one single string having the structure
{{"JD Match":"%","MissingKeywords:[]","Profile Summary":""}}
"""

## streamlit app
st.title("Smart ATS")
st.text("Improve Your Resume ATS")
jd=st.text_area("Paste the Job Description")
uploaded_file=st.file_uploader("Upload Your Resume",type="pdf",help="Please uplaod the pdf")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text=get_text(uploaded_file)
        response=get_response(input_prompt)
        st.subheader(response)




