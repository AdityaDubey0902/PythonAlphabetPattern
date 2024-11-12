from flask import Flask
import os
import time
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get full name
    full_name = "Your Full Name"  # Replace with your actual full name

    # Get system username
    username = os.getenv("USER") or os.getenv("USERNAME")

    # Get server time in IST
    ist_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    # Get `top` command output
    top_output = subprocess.check_output("top -bn1", shell=True).decode("utf-8")

    # Format the output
    output = f"""
    Name: {full_name}<br>
    Username: {username}<br>
    Server Time (IST): {ist_time}<br><br>
    <pre>{top_output}</pre>
    """
    return output

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
