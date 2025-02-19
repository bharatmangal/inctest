from flask import Flask, render_template, redirect, url_for
import subprocess
import platform
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('incognito.html')

@app.route('/open_incognito')
def open_incognito():
    url = "https://example.com"  # URL to open in incognito mode
    system = platform.system()
    try:
        if system == 'Windows':
            # Update chrome_path if your installation is in a different location.
            chrome_path = r"C:\Users\Bharat Coaching Inst\AppData\Local\Google\Chrome\Application\chrome.exe"
            subprocess.Popen([chrome_path, '--incognito', url])
        elif system == 'Darwin':  # macOS
            chrome_path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
            subprocess.Popen([chrome_path, '--incognito', url])
        elif 'ANDROID_ROOT' in os.environ:
            # Likely running on an Android device.
            # The 'am' command is used to start an Android activity.
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

if __name__ == '__main__':
    app.run(debug=True)