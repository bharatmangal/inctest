from flask import Flask, request, render_template, jsonify, session

app = Flask(__name__, template_folder="../templates")
app.secret_key = "supersecretkey"  # Required for session storage

@app.before_request
def verify_access():
    if request.endpoint in ['verify_device', 'static']:
        return  # Allow verification API & static files to load

    if not session.get("verified"):
        return render_template("checking.html")  # Show verification page first

@app.route('/checking')
def checking():
    return render_template('checking.html')

@app.route('/verify_device', methods=['POST'])
def verify_device():
    data = request.get_json()
    camera_count = data.get("camera_count", 0)  # Get camera count from frontend

    if camera_count >= 2:  # Allow if 2 or more cameras are detected
        session["verified"] = True  
        return jsonify({"access": "granted", "redirect": "/index"})
    else:
        return jsonify({"access": "denied", "redirect": "/access_denied"})

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
