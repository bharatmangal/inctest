from flask import Flask, request, render_template
import re

app = Flask(__name__)

@app.before_request
def block_desktop():
    user_agent = request.headers.get('User-Agent', '')
    # Check for common desktop OS indicators
    if re.search(r'(Windows|Macintosh|Linux)', user_agent, re.IGNORECASE):
        return render_template('access_denied.html'), 403

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)