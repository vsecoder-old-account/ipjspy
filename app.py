from flask import Flask, render_template, request
import os, time
from flask import request, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = 'codebinpy'


#index
@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

#ip
@app.route("/ip.js", methods=['GET', 'POST'])
def ip():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    timejs = time.ctime()
    print("IP: " + str(ip))
    return render_template('index.js', ip=ip, timejs=timejs)

#404
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

#RUN
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
