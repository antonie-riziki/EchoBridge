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