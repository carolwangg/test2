import os
from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
    return render_template('main.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
