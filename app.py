# save this as app.py
import functions

import os

from flask import Flask
from flask import render_template, jsonify,request
app = Flask(__name__,template_folder='static')

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/start",methods=['POST'])
async def start():
    params = request.get_json()
    # await os.system(f"python3 main.py -b {params['b']} -d {params['d']}")
    await functions.CustomTimer()
    return jsonify(params)

@app.route("/reports")
def reports():
    return render_template("reports.html")

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)