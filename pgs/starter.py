import streamlit as st

at_url = "https://africastalking.com/"
st.header("Getting Started")

st.subheader("Create an account")

st.markdown("""
    To begin developing with EchoBridge, you'll first need valid Africa’s Talking credentials.  
    Follow this guided process to set up your account and obtain API access.
    """)
st.image('src/img/')

st.info(f"""
        Head to [Africas Talking]({at_url}) and create an account
        """)