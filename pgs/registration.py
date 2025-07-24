import streamlit as st
import pandas as pd
import africastalking
import os
import sys
import requests
import google.generativeai as genai


sys.path.insert(1, './modules')

# from upload_file_rag import get_qa_chain, query_system
from func import welcome_message, send_otp

from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

africastalking.initialize(
    username='EMID',
    api_key = os.getenv("AT_API_KEY")
)

sms = africastalking.SMS
airtime = africastalking.Airtime


@st.dialog("🈴 Vaa Smart Digital Passport")
def digital_passport(first_name, surname, phone_number, email, face_id):
	personal_details, profile_pic = st.columns(2)

	with personal_details:
		st.write(f"<h5 style='text-align: left; margin-bottom: 1px;'>🚺 {str.upper(first_name) + ' ' + str.upper(surname)}</h5>", unsafe_allow_html=True)
		st.write(f"<h5 style='text-align: left; margin-bottom: 1px;'>📬 P.O. Box 00200 </h5>", unsafe_allow_html=True)
		# st.write(f"<h5 style='text-align: left; margin-bottom: 1px;'>📌 {address}, Kenya</h5>", unsafe_allow_html=True)
		st.write(f"<h5 style='text-align: left; margin-bottom: 1px;'>📞 Tel: +254 {phone_number}</h5>", unsafe_allow_html=True)
		# st.write(f"<h5 style='text-align: left; margin-bottom: 1px;'>#️⃣ Site ID: MJ#{site_id}</h5>", unsafe_allow_html=True)
		st.write(f"<h5 style='text-align: left; margin-bottom: 1px;'>📧 Email: {email}</h5>", unsafe_allow_html=True)

	with profile_pic:
		
		if face_id is not None:
			st.image(face_id, width=600)

		else:
	 		st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSdvltpjF8BWal0iwevlrM8ccNwRJDGFxVS6g&s')

	st.write(f"<h5 style='text-align: center; margin-bottom: 1px;'>With your VaaSmart digital profile, track your style preferences, outfit history, local designer interactions, and fashion milestones — a dynamic fashion journey that evolves with you and connects you to new trends and opportunities instantly.</h5>", unsafe_allow_html=True)
	st.write(f"<h5 style='text-align: center; margin-bottom: 1px;'>📑 Terms and Conditions apply</h5>", unsafe_allow_html=True)

	welcome_message(first_name, phone_number)



col1, col2 = st.columns(2)




with col1:
	with st.form(key="user_registration"):
	    st.subheader("Registration")
	    fname, sname = st.columns(2)
	    with fname:
	    	first_name = st.text_input("First Name")
	    with sname:
	    	surname = st.text_input("Surname")
	    
	    username = st.text_input('Username:')
	    email = st.text_input("Email: ")
	    phone_number = st.number_input("Phone Number:", value=None, min_value=0, max_value=int(10e10))
	    password = st.text_input('Passowrd', type="password")
	    confirm_password = st.text_input('Confirm password', type='password')
	    face_id = st.file_uploader('Profile Photo')

	    checkbox_val = st.checkbox("Subscribe to our Newsletter")

	    submit_personal_details = st.form_submit_button("Submit")

	    
	    if password != confirm_password:
	    	st.error('Password mismatch', icon='⚠️')

	    else:
		    
		    if not (email and password):
		    	st.warning('Please enter your credentials!', icon='⚠️')
		    	# st.toast('You Must Register your Personal Details', icon='⚠️')
		    else:
		    	st.success('Proceed to engaging with the system!', icon='👉')

		    	

		    	if submit_personal_details:
		    		digital_passport(first_name, surname, phone_number, email, face_id)



with col2:
	st.image('https://emnaayadi.wordpress.com/wp-content/uploads/2021/11/api-testing.png', width=700)
	st.image('https://miro.medium.com/v2/resize:fit:1358/1*kYc-QYqXO234agRbzjAJsw.png', width=800)
	st.image('https://media.licdn.com/dms/image/v2/D4E12AQHVh5lEW4C7FQ/article-cover_image-shrink_600_2000/article-cover_image-shrink_600_2000/0/1699202062551?e=2147483647&v=beta&t=EXemny6ck7P6xaNjhOryHSoxrUAFyOzdnCLccJBZcRI', width=900)