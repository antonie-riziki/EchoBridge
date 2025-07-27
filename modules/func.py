import string
import random
import secrets
import requests
import re
import os
import bcrypt
import africastalking
import streamlit as st 
import google.generativeai as genai
import base64


from io import BytesIO
from dotenv import load_dotenv
from google.genai import types



import overpy
# from google.generativeai.types import GenerationConfig


load_dotenv()

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

africastalking.initialize(
    username='EMID',
    api_key = os.getenv("AT_API_KEY")
)

nvidia_api = os.getenv("NVIDIA_API_KEY")

sms = africastalking.SMS
airtime = africastalking.Airtime
voice = africastalking.Voice

def send_otp(phone_number, otp_sms):
    # amount = "10"
    # currency_code = "KES"

    recipients = [f"+254{str(phone_number)}"]

    # airtime_rec = "+254" + str(phone_number)

    print(recipients)
    print(phone_number)

    # Set your message
    message = f"{otp_sms}";

    # Set your shortCode or senderId
    sender = 20880

    try:
        # responses = airtime.send(phone_number=airtime_rec, amount=amount, currency_code=currency_code)
        response = sms.send(message, recipients, sender)

        print(response)

        # print(responses)

    except Exception as e:
        print(f'Houston, we have a problem: {e}')

    st.toast(f"OTP Sent Successfully")



def send_drug_reminder(phone_number, time, drug_name):

    recipients = [f"+254{str(phone_number)}"]

    # Set your message
    message = f"You have to take your {drug_name} today at {time} as prescribed. Get well soon!";

    # Set your shortCode or senderId
    sender = 20880

    try:
        response = sms.send(message, recipients, sender)

        print(response)

    except Exception as e:
        print(f'Houston, we have a problem: {e}')

    st.toast(f"Reminder Sent Successfully")




def welcome_message(first_name, phone_number):

    recipients = [f"+254{str(phone_number)}"]

    print(recipients)
    print(phone_number)

    # Set your message
    message = f"Hi {first_name}, Welcome to RxEye! Your digital eye for safe medication use.";

    # Set your shortCode or senderId
    sender = 20880

    try:
        response = sms.send(message, recipients, sender)

        print(response)

    except Exception as e:
        print(f'Houston, we have a problem: {e}')

    st.toast(f"Account Created Successfully")



def make_call(phone_number):    
  
  # Set your Africa's Talking phone number in international format
    callFrom = "+254730731123"
  
  # Set the numbers you want to call to in a comma-separated list
    callTo   = [f"+254{str(phone_number)}"]
    
    try:
  # Make the call
        result = voice.call(callFrom, callTo)
        # print (result)
        return result
    except Exception as e:
        # print ("Encountered an error while making the call:%s" %str(e))
        return f"Encountered an error while making the call:%s" %str(e)



def generate_otp(length=6):
    characters = string.ascii_uppercase + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))



def check_and_encrypt_password(password: str, confirm_password: str):
    
    if password != confirm_password:
        return st.error("Error: Passwords do not match!")

    if len(password) < 8:
        return st.error(f"Error: Password must be at least 8 characters long!")
    
    if not re.search(r"[A-Z]", password):
        return st.error(f"Error: Password must contain at least one uppercase letter!")
    
    if not re.search(r"\d", password):
        return st.error(f"Error: Password must contain at least one number!")
    
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return st.error(f"Error: Password must contain at least one special character!")

    # Encrypt password using bcrypt
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    return st.text_input(label='Encrypted password', value=hashed_password.decode(), type='password')



def autogenerate_code_samples(code_snippet, language):

    model = genai.GenerativeModel("gemini-2.0-flash", 

        system_instruction = f"""
        
            You are a dependable code-conversion assistant. Given a complete Python code snippet (including imports, helper functions, and types)
             and a specified target language, you must generate a **single coherent block** of **fully runnable code** in the target language. 
             Your output must:

            • Preserve all logic, parameter names, return values, and control flow.  
            • Include valid imports or dependencies in the target language (no fictional or hallucinated packages).  
            • Use idiomatic constructs (loops, error handling) and simple, clear comments—easy for beginners.  
            • Provide a minimal entry point (e.g. main(), example usage) so the code runs immediately without modification.  
            • If the target language lacks a direct feature, explicitly note it and provide a real workaround.  
            • Avoid adding features beyond the original Python snippet.  
            • Format only the code (no analysis, no extra text).

            Respond only with the translated code block when a python code snippet as input. 
            """

            )


    response = model.generate_content(
        f"""
        Convert the following Python code to {language}.

        
        {code_snippet}
        
        """,
        generation_config = genai.GenerationConfig(
        max_output_tokens=1000,
        temperature=1.5, 
      )
    
    )
  
    return response.text




