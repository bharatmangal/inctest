from flask import Flask, request, render_template
import re

app = Flask(__name__, template_folder="../templates")

@app.before_request
def block_desktop():
    user_agent = request.headers.get("User-Agent", "").lower()

    # List of common mobile identifiers
    mobile_keywords = ["iphone", "android", "ipad", "mobile"]

    # If no mobile keyword is found, block access
    if not any(keyword in user_agent for keyword in mobile_keywords):
        return render_template("access_denied.html"), 403

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
