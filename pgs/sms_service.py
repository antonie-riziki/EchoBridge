import streamlit as st 
import sys

sys.path.insert(1, './modules')

from code_editor import code_editor
from func import autogenerate_code_samples


st.markdown(
    """
    <div class=title>
        <div style=" justify-content: center;">
            <h3 style="text-align: center; margin-top: -50px; color: #007B8A;">Messaging</h3>
            <p style="text-align: center;">Your API Sandbox and Orchestration Hub.</p>
        </div>
    </div> 
    """,
    unsafe_allow_html=True,
)

st.image('https://miro.medium.com/v2/resize:fit:1000/1*Ulfk0ZmOY71uF9_0aCGmvw.png')

st.info("""
    \n**Bulk SMS**
    \nIntegrate to your service to send branded messages to multiple numbers instantly
    
    \n**Use Case:**
    Used extensively for appointment reminders, transactional updates, promotions, and customer loyalty messages.  
    **Examples:** include healthcare appointment reminders, order and delivery notifications, OTP authentication, and flash sale or loyalty offers.  
    This high‑reach channel ensures timely communication and boosts user engagement.  

""")

st.info("""
    \n**Two-way SMS**
    \nTwo way communication with users and share information or collect feedback from users

    \n**Use Case:**
    Empowers interactive conversations: users can confirm or reschedule appointments, ask questions, participate in surveys, or opt out by replying with a keyword like “STOP.”  
    Ideal for appointment scheduling, service inquiries, customer support, and polls.  


""")

st.info("""
    \n**Premium SMS**
    \nDelivering messages to your users either on demand or subscription 

    \n**Use Case:**
    Also known as reverse‑billing, this charges the recipient for specific content or services (like news alerts, voting, or charity donations).  
    Users actively opt in and receive requested content, while payments are handled via SMS billing systems.  
    This model enables monetized service delivery without requiring external payment gateways.  

""")

st.subheader("Tutorial & Demo")

sample_sms_code = """
    import africastalking
    import os
    from dotenv import load_dotenv

    load_dotenv()

    africastalking.initialize(
        username='USERNAME',
        api_key = os.getenv("AT_API_KEY")
    )


    sms = africastalking.SMS

    def send_message():
        recipients = ["+2547xxxxxxxx"]

        print(recipients)
        print(phone_number)

        # Set your message
        message = "Hello World!";

        # Set your shortCode or senderId
        sender = 20880

        try:
            
            response = sms.send(message, recipients, sender)

            print(response)

        except Exception as e:
            print(f'Houston, we have a problem: {e}')

"""

languages = ["Python", "Node.js", "Javascript", "Ruby", "Typescript", "Rust", "Kotlin", "Php", "Java"]
themes = ["default", "light", "dark", "contrast"]

with st.form('Settings'):
    col1, col2 = st.columns(2)

    with col1:
        language = st.selectbox(label="Select language", options=sorted(languages, reverse=False))
    
    with col2:
        theme = st.selectbox(label="theme", options=themes)

    submit = st.form_submit_button("Submit", type="primary", use_container_width=True)


if submit:
    if language=="Python":
        code = code_editor(sample_sms_code, theme=theme, allow_reset=True, lang='python')

    else:
        
        st.warning("""
            ⚠️ **Warning*:*  
            This code has been automatically generated. Please **review thoroughly, test extensively**, and validate every assumption or edge case before deploying. Do not rely solely on its correctness or security.
        """)
        code_editor(autogenerate_code_samples(sample_sms_code, language), theme=theme, allow_reset=True, lang=language.lower())
        