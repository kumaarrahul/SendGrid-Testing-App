from flask import Flask, request, jsonify, render_template
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os
from dotenv import load_dotenv
import ssl

load_dotenv()
ssl._create_default_https_context = ssl._create_unverified_context
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send-email', methods=['POST'])
def send_email():
    try:
        data = request.json
        message = Mail(
            from_email=os.getenv('FROM_EMAIL'),
            to_emails=data['to'],
            subject=data['subject'],
            plain_text_content=data['message'])
        
        sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
        response = sg.send(message)
        
        return jsonify({
            'success': True,
            'message': 'Email sent successfully!'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True)