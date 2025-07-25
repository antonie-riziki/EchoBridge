import streamlit as st

at_url = "https://africastalking.com/"
st.title("Getting Started")

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

st.image('src/img/Screen Shot 2025-07-24 at 21.22.44.png')

st.info("""

    **Note:** if you have just registered your account, you dont have team yet, so we have to create one

""")
st.subheader('Create a Team')
st.markdown("""
    Click on **New Team** to create a new team
    \nEnter your preffered Team Name, name it something cool 
""")

col1, col2 = st.columns(2)
with col1:
    st.image('src/img/Screen Shot 2025-07-24 at 21.23.01.png')

with col2:
    st.image('src/img/Screen Shot 2025-07-25 at 13.05.16.png')

st.success("""

    **Tip:** Team name **MUST** be a Unique Generic name

""")

st.subheader('Create Application + Add Members')

st.markdown("""

    Once the team is created, we can now proceed to create our application and add 
    memebers to the application and manage other settings of the team. 

""")

st.info("""

    **Note:** As an app owner you can restrict the access levels of your team memebers
    \n as well as data visibility of the application.

""")

col1, col2 = st.columns(2)

with col1:
    st.image('src/img/Screen Shot 2025-07-25 at 13.06.13.png')

with col2: 
    st.image('src/img/Screen Shot 2025-07-25 at 13.06.29.png')

st.success("""

        **Tip:** Note down the **Username** we will be using it as our credential

""")

st.subheader('Account Walkthrough')

st.markdown("""

        Once the application is created, click on the **app** name to access the accounts dashboard of that application

""")

st.image('src/img/Screen Shot 2025-07-25 at 13.42.45.png')

st.info("🎉 Africa’s Talking will deposit **KES 10.00** to your account wallet (for new accounts only)")

st.subheader('Africa’s Talking Products')
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.image('src/img/Screen Shot 2025-07-25 at 13.46.53.png')

with col2:
    st.image('src/img/Screen Shot 2025-07-25 at 13.47.16.png')

with col3:
    st.image('src/img/Screen Shot 2025-07-25 at 13.47.29.png')

with col4:
    st.image('src/img/Screen Shot 2025-07-25 at 13.47.43.png')


col5, col6, col7, col8 = st.columns(4)

with col5:
    st.image('src/img/Screen Shot 2025-07-25 at 13.47.58.png')

with col6:
    st.image('src/img/Screen Shot 2025-07-25 at 13.48.11.png')

with col7:
    st.image('src/img/Screen Shot 2025-07-25 at 13.48.31.png')

with col8:
    st.image('src/img/Screen Shot 2025-07-25 at 13.49.02.png')

st.subheader("API Key Setup")

col1, col2 = st.columns([1, 5])

with col1:
    st.image('src/img/Screen Shot 2025-07-25 at 14.23.05.png', width=380)

with col2:
    st.image('src/img/Screen Shot 2025-07-25 at 14.23.55.png')


st.markdown("""

Congratulations! Your Africa’s Talking account is now active and your API key has been securely generated.  
You are all set to begin coding in your chosen environment whether sandbox/live using your new `username` and `API_KEY`.  
EchoBridge will now authenticate with Africa’s Talking and allow you to simulate or launch real communications (SMS, USSD, Voice, Airtime, Payments) with confidence.

""")

st.warning("""
⚠️ Security Warning:  
\nYour `API_KEY` is a highly privileged secret, treat it like a password. Never share it publicly, commit it to source code (even private repos), 
or expose it in frontend/client-side interfaces. If you suspect any leak, revoke and rotate your key immediately.
""")