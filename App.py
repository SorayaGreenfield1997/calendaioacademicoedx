from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

app = Flask (__name__)
app.secret_key='mysecretkey'

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run (port=5000, debug=True)