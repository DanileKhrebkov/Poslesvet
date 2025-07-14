from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='Главная')

@app.route('/legacy')
def legacy():
    return render_template('legacy.html', title='Legacy')

@app.route('/remastered')
def remastered():
    return render_template('remastered.html', title='Remastered')

@app.route('/forum')
def forum():
    return render_template('forum.html', title='Forum')

@app.route('/second')
def second():
    return render_template('second.html', title='Second')  # Добавляем title\

if __name__ == '__main__':
    app.run(debug=True)