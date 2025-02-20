from flask import Flask, request, render_template, jsonify
import re

app = Flask(__name__, template_folder="../templates")

@app.before_request
def block_desktop():
    user_agent = request.headers.get('User-Agent', '')
    if re.search(r'(Windows|Macintosh|Linux)', user_agent, re.IGNORECASE):
        return render_template('access_denied.html'), 403

@app.route('/')
def checking():
    return render_template('checking.html')  # Start with the verification page

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/access_denied')
def access_denied():
    return render_template('access_denied.html')

@app.route('/verify_device', methods=['POST'])
def verify_device():
    data = request.get_json()
    has_motion = data.get("has_motion", False)

    if has_motion:
        return jsonify({"access": "granted"})
    else:
        return jsonify({"access": "denied"})

if __name__ == '__main__':
    app.run(debug=True)
