import os
from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
    return render_template('main.html')