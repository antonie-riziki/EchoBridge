import streamlit as st 
from st_social_media_links import SocialMediaIcons
from streamlit.components.v1 import html



reg_page = st.Page("./pgs/registration.py", title="register", icon=":material/person_add:")
signin_page = st.Page("./pgs/signin.py", title="sign in", icon=":material/login:")
home_page = st.Page("./pgs/main.py", title="home page", icon=":material/home:")
starter_page = st.Page("./pgs/starter.py", title="Getting started", icon=":material/dry_cleaning:")
setup_page = st.Page("./pgs/setup.py", title="Setup & Installation", icon=":material/theater_comedy:")
# chatbot_page = st.Page("./pgs/chatbot.py", title="chatbot", icon=":material/chat:")

with st.sidebar:
    button = """
        <script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="echominds" data-color="#FFDD00" data-emoji=""  data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#000000" data-coffee-color="#ffffff" ></script>
        """

    html(button, height=70, width=220)
    st.markdown(
        """
        <style>
            iframe[width="220"] {
                position: fixed;
                bottom: 60px;
                right: 40px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


    social_media_links = [
        "https://www.x.com/am_tonie",
        "https://www.youtube.com/@echobytes-ke",
        "https://www.instagram.com/antonie_generall",
        "https://www.github.com/antonie-riziki",
    ]

    social_media_icons = SocialMediaIcons(social_media_links)

    social_media_icons.render()

pg = st.navigation([reg_page, signin_page, home_page, starter_page, setup_page])

st.set_page_config(
    page_title="Echo Bridge",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.echominds.africa',
        'Report a bug': "https://www.echominds.africa",
        'About': """
        
        developer-friendly sandboxed integration platform that lets you plug in your Africa’s Talking credentials, API key and username and 
        immediately start building with SMS, USSD, voice, airtime, and payment services. Begin in sandbox mode (using Africa’s Talking’s sandbox 
        username and test key), simulate your flows, and switch seamlessly to live mode when you’re ready for production 

        As a microservices orchestration hub, EchoBridge is architected to grow. After initial integration with Africa’s Talking, you can plug 
        in additional APIs (like cloud functions, AI endpoints, mapping services, or IoT) without overhauling your core setup."""
    }
)

pg.run()


