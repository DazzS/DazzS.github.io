from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_mail import Message, Mail
import config

DEBUG = True

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'Mashprom.Client@gmail.com'
app.config['MAIL_PASSWORD'] = 'QWEasdZXC123'

mail = Mail(app)

# CORS(app, resources={r"/api/*": {"origins": "*"}})
CORS(app, resources=r'/api/*')

@app.route('/api/send_message', methods=['GET', 'POST'])
def send_mail():
    response_object = {'status': 'none'}
    if request.method == 'POST':
        post_data = request.get_json()

        message_text = {}
        message_text['name'] = post_data.get('name')
        message_text['email'] = post_data.get('email')
        message_text['phoneNumber'] = post_data.get('phoneNumber')
        message_text['message'] = post_data.get('message')

        send_email("Письмо", 'Mashprom.Client@gmail.com', config.ADMINS, "Hello")

        response_object['status'] = 'success'
        print("Работает" )

    return jsonify(response_object)

@app.route('/api/test', methods=['GET', 'POST'])
def test_post():
    data = {'data': 'None'}
    if request.method == 'POST':
        post_data = request.get_json()
        data['data'] = post_data.get('name')
    return jsonify(data)

def send_email(subject, sender, recipients, text_body):
    msg = Message(subject, sender = sender, recipients = recipients)
    msg.body = text_body
    mail.send(msg)

if __name__ == '__main__':
    app.run()