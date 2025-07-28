import streamlit as st 
import sys

sys.path.insert(1, './modules')

from code_editor import code_editor
from func import autogenerate_code_airtime_samples
from sample_tests import send_sample_airtime


st.markdown(
    """
    <div class=title>
        <div style=" justify-content: center;">
            <h3 style="text-align: center; margin-top: -50px; color: #007B8A;">Mobile Data</h3>
            <p style="text-align: center;">Your API Sandbox and Orchestration Hub.</p>
        </div>
    </div> 
    """,
    unsafe_allow_html=True,
)

st.markdown("""
Africa’s Talking’s **Mobile Data API** enables instant distribution of virtual mobile data bundles to subscribers across supported telcos. Through this API, you can send data packages of specified size and validity, manage delivery confirmations via callback, and scale effortlessly—all without managing telco integrations.
""")

st.image('https://surfshark.com/wp-content/uploads/2022/11/Does-VPN-work-on-cellular-data-Hero-1024x501.png')


st.info("""
**Use Case**
\n**Incentivizing Engagement**  
Reward users who participate in surveys, contests, or app referrals with mobile data. Because data is essential and visible, it drives participation and product exploration.

**Onboarding & App Adoption**  
Provide new users with a complimentary data package (e.g. 50 MB) upon signup, helping remove friction and ensuring they can explore your app immediately.

**Agent or Reseller Distribution**  
Enable agent networks or value-added service platforms to distribute data bundles in volume, leveraging discounts and automating delivery and reconciliation processes.

**Micro‑Payment Channels**  
Sell data bundles as micro‑transactions—users can purchase small data packages through your app, with Africa’s Talking handling carrier routing and delivery.
""")