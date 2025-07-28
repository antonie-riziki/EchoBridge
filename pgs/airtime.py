import streamlit as st 
import sys

sys.path.insert(1, ['./modules'])

from code_editor import code_editor
from func import autogenerate_code_samples
from sample_tests import send_sample_message


st.markdown(
    """
    <div class=title>
        <div style=" justify-content: center;">
            <h3 style="text-align: center; margin-top: -50px; color: #007B8A;">Mobile Credit (Airtime)</h3>
            <p style="text-align: center;">Your API Sandbox and Orchestration Hub.</p>
        </div>
    </div> 
    """,
    unsafe_allow_html=True,
)

st.image('https://miro.medium.com/v2/resize:fit:1400/1*x__F1-J_c_VjYFCNCto34Q.jpeg')

st.info("""
    \n**Bulk SMS**
    \nIntegrate to your service to send branded messages to multiple numbers instantly
    
    \n**Use Case:**
    Used extensively for appointment reminders, transactional updates, promotions, and customer loyalty messages.  
    **Examples:** include healthcare appointment reminders, order and delivery notifications, OTP authentication, and flash sale or loyalty offers.  
    This high‑reach channel ensures timely communication and boosts user engagement.  

""")