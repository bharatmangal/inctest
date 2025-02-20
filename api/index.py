from flask import Flask, request, render_template, jsonify, session

app = Flask(__name__, template_folder="../templates")
app.secret_key = "supersecretkey"  # Required for session storage

@app.before_request
def verify_access():
    if request.endpoint in ['verify_device', 'static', 'checking']:
        return  # Allow verification & static files

    if not session.get("verified"):
        return render_template("checking.html")  # Show verification page first

@app.route('/checking')
def checking():
    return render_template('checking.html')

@app.route('/verify_device', methods=['POST'])
def verify_device():
    data = request.get_json()
    camera_count = data.get("camera_count", 0)

    if camera_count >= 2:
        session["verified"] = True  # Store verification in session
        return jsonify({"access": "granted"})
    else:
        return jsonify({"access": "denied"})

@app.route('/index')
def index():
    if not session.get("verified"):
        return render_template("checking.html")
    return render_template('index.html')

@app.route('/access_denied')
def access_denied():
    return render_template('access_denied.html')

if __name__ == '__main__':
    app.run(debug=True)
