import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return 'Routed to index()'

@app.route('/css')
def css():
    return 'Routed to css()'

@app.route('/no_slash')
def no_slash():
    return 'Routed to no_slash()'

@app.route('/optional_slash/')
def optional_slash():
    return 'Routed to optional_slash()'

@app.route('/one/')
@app.route('/one/two/')
@app.route('/three/two/one/')
def multiple():
    return 'Routed to mulitple()'

@app.route('/string/<s>/')
def string_variable(s):
    return 'Routed to string_variable(), s = {}'.format(s)

@app.route('/integer/<int:i>')
def integer_variable(i):
    return 'Routed to integer_variable, i = {}'.format(i)

@app.route('/post_only/', methods=['POST'])
def post_only():
    return 'Routed to post_only()'

if __name__ == '__main__':
    app.run()
