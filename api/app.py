from flask import Flask, render_template, redirect, url_for
import subprocess
import platform
import os

# Set the template folder to "../templates" because this file is in the "api" folder.
app = Flask(__name__, template_folder="../templates")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/open_incognito')
def open_incognito():
    url = "https://example.com"  # URL to open in incognito mode
    system = platform.system()
    try:
        if system == 'Windows':
            # Adjust the Chrome executable path if necessary.
            chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            subprocess.Popen([chrome_path, '--incognito', url])
        elif system == 'Darwin':  # macOS
            chrome_path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
            subprocess.Popen([chrome_path, '--incognito', url])
        elif 'ANDROID_ROOT' in os.environ:
            # For Android devices (if running on one)
            subprocess.Popen([
                "am", "start",
                "-a", "android.intent.action.VIEW",
                "-n", "com.android.chrome/com.google.android.apps.chrome.Main",
                "-d", url,
                "--ez", "create_new_tab", "true",
                "--ez", "incognito", "true"
            ])
        elif system == 'Linux':
            subprocess.Popen(['google-chrome', '--incognito', url])
        else:
            return "Unsupported OS", 500

        return redirect(url_for('index'))
    except Exception as e:
        return f"Error: {str(e)}", 500

# Do not include app.run()—Vercel will import the `app` variable directly.
