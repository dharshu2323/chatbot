import pandas as pd
import streamlit as st

# Load IPC dataset
ipc_data = pd.read_csv('cleaned_dataset.csv')

# Define function to process user query
def process_query(query):
    if 'ipc' in query.lower():
        # Extract the IPC section number from the query
        ipc_section = query.split(' ')[-1]
        # Search for the IPC section in the dataset
        section_info = ipc_data[ipc_data['Description'].str.contains(f'IPC {ipc_section}', case=False, na=False)]
        if not section_info.empty:
            return section_info.iloc[0]['Description']  # Return the description of the IPC section
        else:
            return f"Sorry, I couldn't find information related to IPC section {ipc_section}."
    else:
        # Check if the query is related to sensor values
        if query.lower() in ipc_data.columns:
            latest_value = ipc_data[query.lower()].iloc[-1]
            return f"The latest value of {query} is {latest_value}."
        else:
            return "Sorry, I couldn't find information related to your query."

# Streamlit UI
st.title("IPC Chatbot")

# User input textbox
user_input = st.text_input("You:", "")

# Button to submit query
if st.button("Submit"):
    response = process_query(user_input)
    st.write("Chatbot:", response)
