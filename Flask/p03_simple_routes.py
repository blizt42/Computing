import flask

app = flask.Flask(__name__)

@app.route('/')
def home():
    return 'Welcome'

@app.route('/report')
def generate_report():
    return 'Everything is awesome'

@app.route('/readme.txt')
def readme():
    return 'READ ME'

if __name__ == '__main__':
    app.run()