import streamlit as st 
import sys

sys.path.insert(1, ['./modules'])

from code_editor import code_editor
# from func import autogenerate_code_samples
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