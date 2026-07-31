from flask import Flask, render_template, request


app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    text = "Hello"
    return render_template('base.html', matn=text)


@app.route('/indeks')
def indeks():
    text = "this is about page"
    my_list = [10, 20, 30, 40, 50]
    return render_template('index.html', text=my_list)

@app.template_filter('reversed_string')
def reverse_string(textcha):
    return textcha[::-1]

@app.route('/greet')
def greet():
    namee = request.args.get("nom", 'world')
    return render_template('greet.html', ism=namee)








if __name__ == '__main__':
    app.run(debug=True)
