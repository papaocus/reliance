import openai
import PyPDF2
import os
import streamlit as st

# Set up the OpenAI API client
openai.api_key = "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"

# Open the PDF file
with open('D:/Reliance ChatBot/AR_2021-22.pdf', 'rb') as file:
    # Read the PDF file
    reader = PyPDF2.PdfReader(file)
    # Extract the text from each page
    text = ''
    for i in range(len(reader.pages)):
        page = reader.pages[i]
        text += page.extract_text()

# Define a function to generate a response using GPT-3
def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci",  # Choose the GPT-3 engine to use
        prompt=prompt,     # The user's input prompt
        max_tokens=1024,   # The maximum length of the response
        n=1,               # Generate a single response
        stop=None,         # Stop generating when the response ends
        temperature=0.5,   # The "creativity" of the response
    )
    return response.choices[0].text.strip()

# Define a function to handle user input and generate responses
def handle_input(input_text):
    # Generate a response
    response_text = generate_response(input_text)
    return response_text

# Define the Streamlit app
def app():
    # Set the page title
    st.set_page_config(page_title='Reliance ChatBot')

    # Add a title and subtitle
    st.title('Reliance ChatBot')
    st.markdown('Ask me anything about Reliance!')

    # Define a loop to handle user input and generate responses
    while True:
        # Get user input
        input_text = st.text_input('You', '')
        if input_text:
            # Generate a response
            response_text = handle_input(input_text)
            # Print the response
            st.text_area('Reliance ChatBot', value=response_text, height=200)

# Start the Streamlit app
if __name__ == '__main__':
    app()











        


