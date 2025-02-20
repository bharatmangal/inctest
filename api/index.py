from flask import Flask, request, render_template
import re

app = Flask(__name__, template_folder="../templates")

@app.before_request
def block_desktop():
    user_agent = request.headers.get("User-Agent", "").lower()

    # List of common desktop keywords
    desktop_keywords = ["windows", "macintosh", "linux", "x11"]

    # If any desktop keyword is found, block access
    if any(keyword in user_agent for keyword in desktop_keywords):
        return render_template("access_denied.html"), 403

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
