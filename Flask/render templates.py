from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')

def hw():
    title = 'try render template'
    return render_template('render templates.html', title=title)

if __name__ == '__main__':
    app.run(debug=True)

