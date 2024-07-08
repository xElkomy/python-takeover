from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Your Subdomain takeovered by Cyberar.io Team."
