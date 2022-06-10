from flask import Flask,jsonify,render_template
import socket

app = Flask(__name__)

def fetchDetails():
    hostName = socket.gethostname()
    ip = socket.gethostbyname(hostName)
    return hostName,ip

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"  

@app.route("/health")
def halth():
    return jsonify(
        status="UP"
    )   

@app.route("/details")    
def details():
    hostname,ip=fetchDetails()
    return render_template("index.html",hostname=hostname,ip=ip)