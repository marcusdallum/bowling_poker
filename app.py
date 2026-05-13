from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# Define the directory where the HTML file is located
# Based on previous context, the file is in /home/marcus/Projects/Bowling_Poker/index.html
# or relative to the app.py location.
TEMPLATE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def serve_index():
    """Serves the index.html file at the root URL."""
    return send_from_directory(TEMPLATE_DIR, 'index.html')

@app.route('/rules')
def serve_rules():
    """Serves the rules.md file for reference."""
    return send_from_directory(TEMPLATE_DIR, 'rules.md')

if __name__ == '__main__':
    # Run the server on 0.0.0.0 to make it accessible on the local network
    # This is useful if you are accessing it from a phone connected to the same Wi-Fi
    app.run(host='0.0.0.0', port=5000, debug=True)
