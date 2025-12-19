from flask import Flask, render_template, request, send_from_directory
from werkzeug.middleware.proxy_fix import ProxyFix
import os

passwords = {
        "Tessi":"swivel-casino",
        "Anja":"tropics-landscape" ,
        "Mike":"confess-florist" ,
        "Isa":"bleak-divinely" ,
        "Dani":"research-unopened" ,
        "Joni":"flask-display"
        }

inputNames = list(passwords.keys())

def wichteln(seed:int):
    from itertools import permutations
    import random
    import math

    random.seed(seed)

    numPermutes = math.factorial(len(inputNames))
    names = list(permutations(inputNames))[random.randint(0, numPermutes)]

    mapping = {}

    for index in range(len(names)):
        mapping[names[index]] = names[(index + 1) % len(names)]


    return mapping

app = Flask(__name__)
app.config["APPLICATION_ROOT"] = "/wichtel"
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1, x_prefix=1)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_name = request.form['user_name']
    seed = request.form['seed']
    password = request.form['password']
    try:
        seed = int(seed)
    except:
        error_string = "Seed war keine natürliche Zahl!"
        return render_template('error.html', error_message=error_string)
    
    if user_name not in inputNames:
        error_string = "Unbekannter Name!"
        return render_template('error.html', error_message=error_string)

    if password != passwords[user_name]:
        error_string = "Falsches Passwort!"
        return render_template('error.html', error_message=error_string)

    # You can do more processing here if needed
    mapping = wichteln(seed)
    receiver = mapping[user_name]
    return render_template('response.html', receiver=receiver)

@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory(os.path.join(os.getcwd(),"static"),filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
