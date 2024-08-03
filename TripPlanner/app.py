import os
from dotenv import load_dotenv
import google.generativeai as genai
import streamlit as st
import base64



load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_response(input_prompt):
    model=genai.GenerativeModel("gemini-pro")
    response=model.generate_content(input_prompt)
    return response.text


    

st.set_page_config(page_title="TRIP PLANNER")
st.title("TRIP PLANNER")
source = st.text_input("SOURCE ",key="Source place")

destination = st.text_input("DESTINATION", key = "destination place")
days = st.text_input("DAYS", key = "trip days")


# CSS to inject the background image
with open("trip.jpg", "rb") as img_file:
    img=base64.b64encode(img_file.read()).decode()

# Path to your local image
image_path = 'path/to/your/trip.jpg'


# CSS to inject the background image
page_bg_img = f'''
<style>
body {{
background-image: url("data:image/jpg;base64,{img}");
background-size: cover;
}}
</style>
'''

# Inject CSS with st.markdown
st.markdown(page_bg_img, unsafe_allow_html=True)

# Your Streamlit app content


submit= st.button("trip plan")
if submit :
    input_prompt = f"""
    You are the TRIP PLANNER. You will be provided the source: {source} and destination: {destination}.and the days of trip {days}
    You need to plan the trip according to the given places with a travel plan and its expenses, room to stay, food, and places to visit.
    Example:
    Consider the source is Davangere, and the destination is Mysore.

    Plan:
    Source: Davangere
    Destination: Mysore
    Trip days: 2
    Travel: Train at 12 am, reach Mysore by 8 am. Then check in to your hotel Roopa and visit places like Mysore Zoo, Chamundi Hills.
    Day 2: St. Philomena's Cathedral, Mysore Sand Sculpture Museum, Brindavan Gardens.
    Things to do in Mysore: Mysore Palace, Jagmohan Palace, Radisson Blu Plaza Mysore, The Viceroy, Country Inn and Suites by Radisson.

    provide the complete plan for the trip or vacation which include the travel stay visting places in given days.
    """
    response = get_response(input_prompt)
    st.subheader("Here is your trip plan:")
    st.write(response)
