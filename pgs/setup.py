import streamlit as st 
from code_editor import code_editor

st.title("Getting started")

st.subheader("Prerequisite")

st.markdown("""

    Before we begin, make sure you have the following:

    \n- Python 3.x installed

    \n- An Africa’s Talking account

    \n- A registered sender ID (optional, but ideal for production)

    \n- Username & API key 

""")

st.subheader("Installation")



# Python installation 
st.write('- **Python**')
st.write('Run this in your Terminal')
st.code("""
    # install required dependancies (pip)
    pip install africastalking python-dotenv
    """)
st.write('Copy to your Script')
st.code("""
    import africastalking
    import os
    from dotenv import load_dotenv

    load_dotenv()

    africastalking.initialize(
        username='YOUR_USERNAME',
        api_key = os.getenv("AT_API_KEY")
    )

""")
# code_editor('pip install africastalking python-dotenv', lang='python')



# Noje.js & JavaScript installation 
st.write('- **Node.js / JavaScript**')

st.write('Run this in your Terminal')
st.code("""
    # install required dependancies (npm)
    npm install africastalking
    """)

st.write('Copy to your Script')
st.code("""
    const AfricasTalking = require('africastalking')({
        apiKey: process.env.AT_API_KEY,
        username: process.env.AT_USERNAME
    });
""")
# code_editor('pip install africastalking python-dotenv', lang='python')




# Ruby installation 
st.write('- **Ruby**')

st.write('Run this in your Terminal')
st.code("""
    # install required dependancies (npm)
    gem 'africastalking-ruby'
    """)

st.write('Copy to your Script')
st.code("""
    require "AfricasTalking"

    username = "USERNAME"      
    api_key  = "YOUR_API_KEY" 

    at = AfricasTalking::Initialize.new(username, api_key)

""")
# code_editor('pip install africastalking python-dotenv', lang='python')