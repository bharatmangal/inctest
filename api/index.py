from flask import Flask, request, render_template, jsonify

app = Flask(__name__, template_folder="../templates")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/access_denied")
def access_denied():
    return render_template("access_denied.html")

@app.route("/verify_device", methods=["POST"])
def verify_device():
    data = request.json
    has_motion = data.get("has_motion", False)

    if not has_motion:
        return jsonify({"access": "denied"}), 403
    return jsonify({"access": "granted"})

if __name__ == "__main__":
    app.run(debug=True)
