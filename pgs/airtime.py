import streamlit as st 
import sys

sys.path.insert(1, './modules')

from code_editor import code_editor
from func import autogenerate_code_airtime_samples


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
st.markdown("""
With the Airtime API from Africa’s Talking, you can effortlessly distribute *virtual, pinless airtime* to mobile users across supported countries. Transactions are handled securely via API endpoints, and delivery status is pushed back to your system through callbacks—no manual telco integration required.
""")

st.image('https://miro.medium.com/v2/resize:fit:1400/1*x__F1-J_c_VjYFCNCto34Q.jpeg')


st.info("""
**Use Cases**
\n**User Incentives & Promotions**  
Reward users—such as referring a friend, completing a survey, or participating in a campaign—with airtime credits instantly delivered to their phone. This increases engagement and drives uptake.

**Agent & Reseller Platforms**  
Create systems where agents or resellers distribute airtime at scale, benefiting from volume discounts and real-time transaction validations.

**Corporate Allowance Programs**  
Disburse airtime allowances to staff or field agents directly through your application, automating routine top‑ups and tracking usage centrally for transparency.
""")


st.subheader("Tutorial & Demo")

sample_airtime_code = """
    import africastalking
    import os
    from dotenv import load_dotenv

    load_dotenv()

    africastalking.initialize(
        username='USERNAME',
        api_key = os.getenv("AT_API_KEY")
    )


    airtime = africastalking.Airtime

    def send_message():
        amount="10"
        currency_code = "KES"
        
        recipients = "+254" + str(phone_number)

        print(recipients)
        print(phone_number)

        try:
            responses = airtime.send(phone_number=recipients, amount=amount, currency_code=currency_code)

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
        code = code_editor(sample_airtime_code, theme=theme, allow_reset=True, lang='python')

    else:
        
        st.warning("""
            **⚠️ Warning:**  
            This code has been automatically generated. Please **review thoroughly, test extensively**, and validate every assumption or edge case before deploying. Do not rely solely on its correctness or security.
        """)
        
        final_code_snippet = st.code(autogenerate_code_airtime_samples(str(sample_airtime_code), language), language=language)


st.markdown("""

    Live Environment

""")

with st.container(border=True):
    sample_message = ""
    
    test_key = st.text_input('**API KEY**', type="password")
    
    col1, col2 = st.columns(2)
    
    with col1:
        test_username = st.text_input('**Username**')
        test_phone_number = st.number_input("**Phone Number:**", value=None, min_value=0, max_value=int(10e10))

    with col2:
        text_choice = st.selectbox("**Currency Code**", options=["KES", "USD", "UGX", "TZS", "ZMW", "JPY"])
        amount = st.number_input("**Amount:**", value=None, min_value=0, max_value=int(10e10))

with st.form("Test Environment"):
    test_submission = st.form_submit_button("**Test**", type="primary", use_container_width=True)

    if test_submission and test_key and test_username and test_phone_number and sample_message is not None:
        response = send_sample_message(test_key, test_username, test_phone_number, sample_message)
        st.code(response)

    else:
        st.warning("""
        
            **Warning:**
            \nKindly Fill in Your Credentials **API_KEY** or **USERNAME** before proceeding

        """)

    