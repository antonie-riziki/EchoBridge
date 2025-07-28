
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




def send_sample_airtime(test_key, test_username, test_phone_number, test_currency_code, test_amount):

    africastalking.initialize(
        username=test_username,
        api_key =test_key
    )

    airtime = africastalking.Airtime


    # Target Recipients List
    recipients= "+254" + str(test_phone_number)

    #Set Your Message
    amount = str(test_amount)

    currency_code = test_currency_code

    try:
        response = airtime.send(phone_number=recipients, amount=amount, currency_code=currency_code)

        return response

    except Exception as e:
        return f'Houston, we have a problem: {e}'
        return st.error("""

            **Error**
            \nCheck Your Credentials

        """)