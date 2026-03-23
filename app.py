from flask import Flask, render_template, request
from scanner import scan_network

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    devices = []

    if request.method == "POST":

        ip_range = request.form.get("ip")

        devices = scan_network(ip_range)

    return render_template("index.html", devices=devices)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
