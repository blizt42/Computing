from flask import *

app = Flask(__name__)

@app.route('/A/')
def view_A():
    return render_template('A.html')

@app.route('/B/')
def view_B():
    return render_template('B.html')

if __name__ == '__main__':
    app.run()