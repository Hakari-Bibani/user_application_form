from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
load_dotenv()

EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        english_level = request.form['english_level']
        python_level = request.form['python_level']
        experience = request.form['experience']

        # Check if the user meets the acceptance criteria
        if english_level == '3' and python_level == '3' and experience == '5+ years':
            subject = "Application Accepted!"
            body = f"Dear {name},\n\nWe are delighted to inform you that your application for our course has been accepted!"
        else:
            subject = "Application Declined"
            body = f"Dear {name},\n\nThank you for your interest in our course, but unfortunately, we cannot offer you a place at this time."

        send_email(email, subject, body)

    return render_template('form.html')

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

