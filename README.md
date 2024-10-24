# User Application Form with Email Response

## Overview
This Flask-based web application collects user details and automatically sends personalized emails based on their responses.

### Features:
- Collect user information (Name, Email, Experience, etc.)
- Automatically send customized email based on user's qualifications.

### Setup Instructions:
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file with your email credentials.
4. Run the Flask app: `python app.py`
5. Visit `http://127.0.0.1:5000` in your browser.

### Project Structure:
- `app.py`: Main application logic.
- `templates/form.html`: HTML form for user input.
- `user_data.csv`: Stores user information.
