import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT')

def send_email(to, subject, body):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_USER
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
    server.starttls()
    server.login(EMAIL_USER, EMAIL_PASSWORD)
    text = msg.as_string()
    server.sendmail(EMAIL_USER, to, text)
    server.quit()

# Streamlit UI
st.title('Personal Information Form')

# Form inputs
name = st.text_input("Name")
dob = st.date_input("Date of Birth")
mobile = st.text_input("Mobile Number")
email = st.text_input("Email")
english_level = st.selectbox("Level of English Language", ["1 - Beginner", "2 - Intermediate", "3 - Advanced"])
python_level = st.selectbox("Level of Python", ["1 - Beginner", "2 - Intermediate", "3 - Advanced"])
experience = st.selectbox("Experience", ["Less than a year", "2-4 years", "5+ years"])

# Submit button
if st.button('Submit'):
    if english_level == '3 - Advanced' and python_level == '3 - Advanced' and experience == '5+ years':
        subject = "Application Accepted!"
        body = f"Dear {name},\n\nWe are delighted to inform you that your application for our course has been accepted!"
        send_email(email, subject, body)
        st.success("Application accepted! Email sent.")
    else:
        subject = "Application Declined"
        body = f"Dear {name},\n\nThank you for your interest in our course, but unfortunately, we cannot offer you a place at this time."
        send_email(email, subject, body)
        st.warning("Application declined. Email sent.")
