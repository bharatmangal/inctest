from flask import Flask, request, render_template
import re

app = Flask(__name__, template_folder="../templates")

@app.before_request
def block_desktop():
    if request.endpoint == "static":
        return  # Allow static files

    user_agent = request.headers.get("User-Agent", "")
    if re.search(r"(Windows|Macintosh|Linux)", user_agent, re.IGNORECASE):
        return render_template("access_denied.html"), 403

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
