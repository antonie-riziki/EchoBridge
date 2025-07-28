
import africastalking
import streamlit as st 

def send_sample_message(test_key, test_username, test_phone_number, test_message):

    africastalking.initialize(
        username=test_username,
        api_key =test_key
    )

    sms = africastalking.SMS


    # Target Recipients List
    recipients=[f"+254{str(test_phone_number)}"]

    #Set Your Message
    message = test_message;

    # Set your shortCode or senderId
    sender = 20880

    try:
        response = sms.send(message, recipients, sender)

        return response

    except Exception as e:
        return f'Houston, we have a problem: {e}'
        return st.error("""

            **Error**
            \nCheck Your Credentials

        """)


