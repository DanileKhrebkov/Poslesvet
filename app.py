from flask import Flask, render_template
from flask_bootstrap import Bootstrap  # Изменили импорт

app = Flask(__name__)
bootstrap = Bootstrap(app)  



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/page1')
def page1():
    return render_template('page1.html', 
                         title="Afterglow: Remastered",
                         content=("ДИСКЛЕЙМЕР: Все действия мода разворачиваются в выдуманной вселенной, все персонажи достигли возраста 18 лет, все совпадения случайны"
                                  ""
                                  ),
                         image_url="images/service.jpg")

@app.route('/page2')
def page2():
    return render_template('page2.html', 
                         title="Afterglow 2: Empty Borders",
                         content=("ДИСКЛЕЙМЕР: Все действия мода разворачиваются в выдуманной вселенной, все персонажи достигли возраста 18 лет, все совпадения случайны"
                                  ""
                                  ),
                         image_url="images/about.jpg")

@app.route('/page3')
def page3():
    return render_template('page3.html', 
                         title="Afterglow: Legacy",
                         content=("ДИСКЛЕЙМЕР: Все действия мода разворачиваются в выдуманной вселенной, все персонажи достигли возраста 18 лет, все совпадения случайны"
                                  ""
                                  ),
                         image_url="images/contacts.jpg")

if __name__ == '__main__':
    app.run(debug=True)