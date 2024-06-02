import os
import streamlit as st
from src.mcqgener.MCQGenerator import generate_evaluate_chain
from src.mcqgener.logger import logging
from src.mcqgener.utils import get_data, get_table_data
import json
import traceback
# Loading json file:

with open("C:\Users\amir\mcqgenerator\RESPONSE.json", "r") as file:
    RESPONSE_JSON = json.load(file)


# Creating a title for out app :
st.title("MCQs Generator using Langchain ")

# Create a form using st.form

with st.form("User_inputs"):
    uploaded_file = st.file_uploader("Upload file:")
    #Input fields
    mcq_count = st.number_input("Nb of MCQS", min_value=3, max_value=8)
    mcq_subject = st.text_input("Insert Subject", max_chars=20)
    mcq_tone = st.text_input("Tone: ", max_chars=10, placeholder="Simple")

    # Add button to submit the fprm
    button = st.form_submit_button("Create MCQs")

    # Chekc if button is clicked and other options are not NOne:
    if button and uploaded_file is not None and mcq_count and mcq_subject and mcq_tone:
        with st.spinner("Loading answer ..."):
            try:
                text = get_data(uploaded_file)
                response = response = generate_evaluate_chain(
                    {
                        "text":text,
                        "number":mcq_count,
                        "subject":mcq_subject,
                        "tone":mcq_tone,
                        "response_json":json.dumps(RESPONSE_JSON)
                    }
                )
            except Exception as e:
                traceback.print_exception(type(e), e, e.__traceback__)
                st.error("Error")
            
            else:

                if isinstance(response, dict):
                    # Extract the quiz data from the response:
                    quiz = response.get("quiz")

                    lines = quiz.split("\n")
                    quiz_str = "\n".join(lines[1:])


                    quiz = json.loads(quiz_str)
                    if quiz is not None:
                        table_data = get_table_data(quiz)
                        if table_data is not None:
                            st.table(table_data)
                            review = response.get("review")
                            st.text_area(label="Review", value=review)

                        else:
                            st.error("Error in the table data")
                else:
                    st.write(response)
