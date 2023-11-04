from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_url_path="", static_folder="templates")


@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(host="localhost", port=5555, debug=True, threaded=False)
