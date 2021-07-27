import flask as f

vowels = ['a', 'e', 'i', 'o', 'u']
app = f.Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if f.request.method == 'GET':
        return f.render_template('form_with_post.html')
    if 'string' in f.request.form:
        s = f.request.form['string']
        lower_s = s.lower()
        num_vowels = 0
        num_numbers = 0
        greet = False
        text = 'hi, nice to meet you!'
        for vowel in vowels:
            num_vowels += lower_s.count(vowel)
        for num in range(len(s)):
            if s[num].isdigit():
                num_numbers += 1
        for word in lower_s.split():
            if word == 'hello':
                greet = True
        num_words = len(lower_s.split())
        return f.render_template('analysis_results.html', s=s,num_vowels= num_vowels, num_words = num_words, num_numbers =num_numbers , text = text
                                 , greet = greet)
    return 'no form data found'

if __name__ == '__main__':
    app.run()