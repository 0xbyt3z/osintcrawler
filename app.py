# save this as app.py
import functions


from flask import Flask
from flask import render_template, jsonify, request
app = Flask(__name__, template_folder='static')


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/start", methods=['POST'])
async def start():
    try:
        params = request.get_json()
        await functions.runCommand(f"python3 main.py -b {params['b']} -d {params['d']}")
        # if(params["b"] == "google"):
        #     return jsonify(email=functions.getEmails())
        # if(params["b"] == "twitter"):
        #     return jsonify(twitter=functions.getTwitter())
        # if(params["b"] == "linkedin"):
        #     return jsonify(linkedin=functions.getLinkedin()())
        return jsonify(email=functions.getEmails(), twitter=functions.getTwitter(), linkedin=functions.getLinkedin())
    except:
        return jsonify(["null"])


@app.route("/read", methods=['POST'])
async def read():
    try:
        return jsonify(email=functions.getEmails(), twitter=functions.getTwitter(), linkedin=functions.getLinkedin())
    except:
        return jsonify(["null"])


@app.route("/clear", methods=['POST'])
async def clear():
    try:
        functions.clearFiles()
        return jsonify(msg="done")
    except:
        return jsonify(msg="failed")


@app.route("/reports")
def reports():
    return render_template("reports.html")


if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)
