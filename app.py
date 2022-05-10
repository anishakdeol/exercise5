from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug import exceptions
# from flask_mail import Mail, Message

app = Flask(__name__)
CORS(app)

# app.config['DEBUG'] = True
# app.config['TESTING'] = False
# app.config['MAIL_SERVER']='smtp.husmail.com'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USERNAME'] = 'anisha@prettyprinted.com'
# app.config['MAIL_PASSWORD'] = ''
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USE_SSL'] = False
# # app.config['MAIL_DEBUG'] = True
# app.config['AIL_DEFAULT_SENDER'] = 'anisha@prettyprinted.com'
# app.config['MAIL_MAX_EMAILS'] = 5
# # app.config['MAIL_SUPPRESS_SEND'] = False
# app.config['MAIL_ASCI_ATTACHMENTS'] = False
# mail = Mail(app)



# @app.route('/')
# def index():
#     msg = Message('Hello', recipients = ['jeyew26081@eoscast.com'])
#     mail.send(msg)

#     return 'Message has been sent'

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
    app.run()
