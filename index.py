from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/api')
def api():
    with open('data.json', mode='r') as my_data_file:
        text = my_data_file.read()
        return text
