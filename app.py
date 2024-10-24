from flask import Flask, render_template, request
import pandas as pd
import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

# Load environment variables (for email credentials)
load_dotenv()

app = Flask(__name__)

# Route for the form page
@app.route('/')
def form():
    return render_template('form.html')

# Route for form submission
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    dob = request.form['dob']
    mobile = request.form['mobile']
    email = request.form['email']
    english_level = request.form['english_level']
    python_level = request.form['python_level']
    experience = request.form['experience']

    # Save to CSV file
    data = {'Name': name, 'Date of Birth': dob, 'Mobile': mobile, 'Email': email, 
            'English Level': english_level, 'Python Level': python_level, 'Experience': experience}
    df = pd.DataFrame([data])
    df.to_csv('user_data.csv', mode='a', header=False, index=False)

    # Check if user meets criteria
    if english_level == '3' and python_level == '3' and experience == '5+':
        send_email(email, name, 'accept')
        return f"Thank you {name}, your application has been accepted!"
    else:
        send_email(email, name, 'decline')
        return f"Thank you {name}, unfortunately, your application was not accepted at this time."

# Function to send an email
def send_email(user_email, user_name, status):
    sender_email = os.getenv('EMAIL')
    sender_password = os.getenv('PASSWORD')
    
    if status == 'accept':
        subject = "Course Acceptance"
        body = f"Dear {user_name},\n\nWe are delighted to inform you that your application has been accepted!"
    else:
        subject = "Course Declined"
        body = f"Dear {user_name},\n\nThank you for your interest. Unfortunately, we cannot offer you a place at this time."
    
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = user_email
    msg.set_content(body)

    # Connect to the email server
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)

if __name__ == "__main__":
    
