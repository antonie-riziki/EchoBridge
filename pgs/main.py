
from __future__ import annotations

import streamlit as st 
import sys

from datetime import datetime, timedelta


sys.path.insert(1, './modules')
print(sys.path.insert(1, '../modules/'))


from dotenv import load_dotenv

load_dotenv()



st.markdown(
    """
    <div class=title>
        <div style=" justify-content: center;">
            <h1 style="text-align: center; margin-top: -50px; color: #007B8A;">Echo Bridge 🎯</h1>
            <p style="text-align: center;">Your API Sandbox and Orchestration Hub.</p>
        </div>
    </div> 
    """,
    unsafe_allow_html=True,
)

st.image('https://qameta.io/assets/cover.63b103c6.png', width=700)


st.subheader("Welcome to EchoBridge")

st.markdown("""

    EchoBridge is a secure, sandbox‑style platform built with Streamlit that lets you integrate
    with Africa’s Talking services [SMS, USSD, Voice, Airtime, and Payments] using your API key
    and username. Switch between sandbox and live environments seamlessly. .
    
    """)

st.info("""
        **Note:**
        Designed from day one to be modular, EchoBridge is ready to grow with additional microservice integrations
        
        """)

st.subheader("About the System")
st.markdown("""
    
    This application provides a unified, developer friendly interface for testing and deploying
    communication and payment workflows via Africa’s Talking. Operations like sending SMS,
    designing USSD menus, triggering voice calls, distributing airtime, and processing mobile
    payments are all accessible through a consistent UI layer.  
    
    
    
    """)

st.info(""" 
        **Note:**
        By abstracting provider-specific details into adapters, EchoBridge remains flexible and extensible, ready to absorb new APIs in the future.
        
        """)

st.subheader("What to Expect")
st.markdown("""
    
    Initially, you’ll work in sandbox mode: no charges, no risk, just simulation. Once you’re ready,
    flip to live mode and plug in your production credentials.

    You will find:
    - A clean Dashboard showing API activity
    - Toggle controls for sandbox vs production
    - Configuration panels for Africa’s Talking credentials
    - Embedded documentation, code examples, and quick‑start guides
    - Webhook registration for callbacks like delivery receipts, USSD inputs, and payments
    
    """)

st.info(""" **Note:**
        EchoBridge offers a safe, isolated sandbox where you can experiment with real‑world SMS, USSD, voice,
        airtime, and payment flows without affecting live systems or incurring charges. Expect full control over 
        test scenarios, realistic API behaviors, and clean separation from production data—all designed for safe development and debugging.
        """)

st.success("""
        **Tip:** Use data in the sandbox that mirrors your real use cases and test error‑handling paths thoroughly, you will uncover issues early and avoid surprises in production.
        """)


st.subheader("Code of Conduct")
st.markdown("""
    
    This project embraces a respectful and inclusive environment. Harassment, hate speech, or
    any unprofessional behavior is strictly prohibited. Conversations should remain courteous,
    collaborative, and solution‑oriented. Users must not share personal credentials or sensitive data
    publicly. Any violation of these norms may result in removal from the platform or community forums.
    
    """)


st.subheader("Policy Overview")
st.markdown("""
    
    Your data privacy matters. EchoBridge collects minimal personal data (e.g. email, usage logs)
    only as needed to operate the service. We do not share your credentials or personal details.
    You may access, modify, or delete your data per applicable data protection rules.
    
    """)

st.warning("""
        **Warning:** Violations of our Code of Conduct or Terms, such as spam messaging, credential sharing, or misuse of services may result in immediate suspension or termination of access.
        """)



st.subheader("Terms & Conditions")
st.markdown("""
    
    By using EchoBridge, you agree to operate within permitted use: testing and development
    with sandbox credentials, and lawful communication when live. Abuse of SMS, USSD, Voice,
    Airtime, or Payments services—such as spam or fraudulent activity—is prohibited. EchoBridge
    makes no warranty regarding uninterrupted availability and limits liability as allowed by law.
    We may suspend or terminate access for misuse or violation of these terms.
    
    """)


