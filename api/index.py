from flask import Flask, request, render_template
import re

app = Flask(__name__, template_folder="../templates")

@app.before_request
def block_desktop():
    user_agent = request.headers.get('User-Agent', '')
    if re.search(r'(Windows|Macintosh|Linux)', user_agent, re.IGNORECASE):
        return render_template('access_denied.html'), 403

@app.route('/')
def index():
    return render_template('index.html')

# Vercel needs a handler function
def handler(request, *args, **kwargs):
    return app(request.environ, start_response)
