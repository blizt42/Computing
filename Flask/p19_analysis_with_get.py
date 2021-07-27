import flask as f

vowels = ['a', 'e', 'i', 'o', 'u']

app = f.Flask(__name__)

@app.route('/')
def form():
    return f.render_template('form_with_get.html')

@app.route('/process/')
def process_with_get():
    if 'string' in f.request.args:
        s = f.request.args['string']
        lower_s = s.lower()
        num_vowels = 0
        for vowel in vowels:
            num_vowels += lower_s.count(vowel)
        num_words = len(s.split())
        return f.render_template('analysis_results.html', s=s, num_vowels = num_vowels, num_words = num_words)
    return 'No form data formed'

if __name__ == '__main__':
    app.run()