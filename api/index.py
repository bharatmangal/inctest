from flask import Flask, request, render_template, jsonify

app = Flask(__name__, template_folder="templates")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/verify_device", methods=["POST"])
def verify_device():
    data = request.json
    is_mobile = data.get("is_mobile", False)

    if not is_mobile:
        return jsonify({"access": "denied"}), 403
    return jsonify({"access": "granted"})

if __name__ == "__main__":
    app.run(debug=True)
