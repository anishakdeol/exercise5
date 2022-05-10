from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug import exceptions
from flask_mail import Mail, Message

app = Flask(__name__)
CORS(app)
mail = Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'yourId@gmail.com'
app.config['MAIL_PASSWORD'] = '*****'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

@app.route("/")
def index():
    msg = Message('Hello', sender = 'yourId@gmail.com', recipients = ['someone1@gmail.com'])
    msg.body = "This is the email body"
    mail.send(msg)
    return "Sent"

@app.route('/')
def home():
    return 'Welcome to our API. By Anisha, Ikenna and Sarushan'

animes = [
    {'id': 1, 'name': 'Bubble', 'year': 2022},
    {'id': 2, 'name': 'Blackover', 'year': 2017},
    {'id': 3, 'name': 'Blue Period', 'year': 2021}
]
@app.route('/anime', methods=['GET', 'POST'])
def anime():
    if request.method == 'GET':
        return jsonify(animes)  
    if request.method == 'POST':
        data = request.json
        data['id'] = len(animes) + 1
        animes.append(data)
        return f"{data['name']} has been added to the anime list!"

@app.errorhandler(exceptions.NotFound)
def handle__404(err):
    return jsonify({"message": f"Oops... {err}"}), 404

@app.errorhandler(exceptions.InternalServerError)
def handle_server_error(err):
    return jsonify({"message": f"{err}. It's not you, it's us. Press F to pay respects"}), 500

if __name__ == '__main__':
    app.run(debug=True)
