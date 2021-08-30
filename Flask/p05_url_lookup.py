from flask import *

app = Flask(__name__)

@app.route('/')
def home():
    url1 = url_for('fixed_route')
    url2 = url_for('string_variable', s = 'example')
    url3 = url_for('integer_variable', i = '2021')
    print(url1)
    print(url2)
    print(url3)
    return 'Check your shell or command prompt window'

@app.route('/fixed/')
def fixed_route():
    return 'Routed to fixed_route()'

@app.route('/string/<s>')
def string_variable(s):
    return 'Routed to string_variable(), s = {}'.format(s)

@app.route('/integer/<int:i>')
def integer_variable(i):
    return 'Routed to integer_variable, i = {}'.format(i)

if __name__ == '__main__':
    app.run()

