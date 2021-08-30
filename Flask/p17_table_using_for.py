from flask import *

app = Flask(__name__)

@app.route('/')
def home():
    results ={
        'Math': 78,
        'Physics': 90,
        'Computing': 100,
        'Geography': 60
    }
    return render_template('table.html', results= results)

if __name__ == '__main__':
    app.run()

