import streamlit as st
import pandas as pd
import smtplib
from email.mime.text import MIMEText

# Function to send email
def send_email(name, email, message):
    # Set up your SMTP server credentials
    smtp_server = 'smtp.gmail.com'  # Gmail SMTP server
    smtp_port = 587  # Port for TLS
    smtp_user = 'meermiro299@gmail.com'  # Your email address
    smtp_password = 'your_app_password_here'  # Your app password (if 2FA enabled)

    msg = MIMEText(message)
    msg['Subject'] = 'Application Status'
    msg['From'] = smtp_user
    msg['To'] = email

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Secure the connection
        server.login(smtp_user, smtp_password)
        server.send_message(msg)

# Streamlit form
st.title('Personal Information Form')
with st.form(key='application_form'):
    name = st.text_input('Name:')
    dob = st.date_input('Date of Birth:')
    mobile = st.text_input('Mobile number:')
    email = st.text_input('Email:')
    english_level = st.selectbox('Level of English language:', ['1 - Beginner', '2 - Intermediate', '3 - Advanced'])
    python_level = st.selectbox('Level of Python:', ['1 - Beginner', '2 - Intermediate', '3 - Advanced'])
    experience = st.selectbox('Experience:', ['Less than a year', '2-4 years', '5+ years'])

    submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        # Process the form data
        if english_level == '3 - Advanced' and python_level == '3 - Advanced' and experience == '5+ years':
            message = f"Dear {name},\n\nWe are delighted to inform you that your application for our Course has been accepted! We are excited to have you join us.\n\nYou will be hearing from us soon with more details about the course."
        else:
            message = f"Dear {name},\n\nThank you for your interest in our Course. We appreciate you taking the time to apply. Unfortunately, due to limited enrollment or other factors, we are unable to offer you a place in this particular course at this time. We understand that this may be disappointing, and we apologize for any inconvenience. Please know that we will keep your application on file and will inform you of any future opportunities or similar courses that may be of interest to you."

        # Send the email
        send_email(name, email, message)
        st.success("Your application has been submitted. Check your email for the response.")
