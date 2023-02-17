# If you don't have python installed, or don't want to install 
# any required libraries (like openai and questionary)
# you can do this workshop online from 
# https://replit.com/@sus118/AskGPT-CLI-Tool#INSTRUCTIONS-README.MD

import openai
import yaml
import string
import questionary

# Set OpenAI API key
openai.api_key_path = 'apikey.file'


# Load prompt templates from a YAML file. Prompts may or may not have placeholders for user inputs.



# Define a function to fill in the prompt template
# - Parse the prompt template to find placeholders and ask the user to fill them in
# - Substitute the filled placeholders into the prompt template



# Define a function to generate a GPT response to a given prompt
# - Use OpenAI's Completion API to generate a response to the prompt
# - Extract the GPT-generated answer from the API response
    

# Main program entry point
# - Ask the user to select an action
# - If the user selects "freetext", ask for a prompt
# - Otherwise, fill in the prompt template for the selected task
# - Generate a GPT response to the prompt and print it
