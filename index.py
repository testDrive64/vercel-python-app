from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/info')
def info():
    return "Dies ist ein Platzhalter für die Eigentliche Story."


@app.route('/api')
def api():
    with open('data.json', mode='r') as my_data_file:
        text = my_data_file.read()
        return text
