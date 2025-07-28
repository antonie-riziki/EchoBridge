import streamlit as st 
import sys

sys.path.insert(1, './modules')

from code_editor import code_editor


st.markdown(
    """
    <div class=title>
        <div style=" justify-content: center;">
            <h3 style="text-align: center; margin-top: -50px; color: #007B8A;">USSD</h3>
            <p style="text-align: center;">Your API Sandbox and Orchestration Hub.</p>
        </div>
    </div> 
    """,
    unsafe_allow_html=True,
)


st.markdown("""
Africa’s Talking provides a robust **USSD (Unstructured Supplementary Service Data) API** that enables interactive, session-based mobile applications accessible on *all* phones—even without internet. Users dial a short code (like *483#) and interact with your service in real time through menus and prompts, facilitated via callback URLs.
""")

st.image('https://res.cloudinary.com/startup-grind/image/upload/c_fill,dpr_2.0,f_auto,g_center,h_540,q_100,w_1080/v1/gcs/platform-data-africastalking/blog/Post.png')


st.info("""
**Use Cases**
\n**Service Access & Information Lookup**  
Offer menu-driven services like airtime balance checks, appointment confirmations, or information retrieval (e.g., weather, crop tips). Perfect for users without internet or with feature phones.

**Registration & Form Data Collection**  
Deploy USSD workflows to capture structured user input—such as name, ID number, or feedback—during sign-up flows or surveys. USSD ensures high reach and simplicity in data gathering.

**Service Requests & Transactions**  
Enable features like cab bookings, order placement, bill inquiry, or loan applications. USSD flows integrate with backend systems to retrieve, validate, and process requests instantly.

**Payments & Micro‑Transactions**  
Trigger seamless USSD-based menus for mobile payments or checkout flows. For example, users might dial a code to initiate a wallet transfer or paybill transaction via Africa’s Talking Payments integration.
""")