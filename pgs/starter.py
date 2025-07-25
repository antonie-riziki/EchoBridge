import streamlit as st

at_url = "https://africastalking.com/"
st.header("Getting Started")

st.subheader("Create an account")

st.markdown("""
    To begin developing with EchoBridge, you'll first need valid Africa’s Talking credentials.  
    Follow this guided process to set up your account and obtain API access.
    """)
st.image('src/img/Screen Shot 2025-07-24 at 17.20.46.png')

st.info(f"""
        **Note:** Visit [africastalking.com]({at_url}) and create an account
        """)

st.write("""
    after clicking on login, a new window will load for user autherntication processes
    \n- You can either create an account (if you dont have) or 
    \n- Enter your login credentials (email and password)

        """)

st.image('src/img/Screen Shot 2025-07-24 at 17.16.18.png')
st.success("""

    **Tip:** You can login using either Github, Google or Microsoft account

    """)

st.write("""
       the Sandbox window below will be displayed, where you can 
       \n- Edit & Update your profile
       \n- View Documentation
       \n- Go to AT Sandbox
""")

st.image()

st.info("""

    **Note:** if you have just registered your account, you dont have team yet, so we have to create one

""")

st.markdown("""
    
""")