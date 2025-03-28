#Импорт
from flask import Flask, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
#Подключение SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Создание db
db = SQLAlchemy(app)

#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')


#Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_telegram = request.form.get('button_telegram')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')
    return render_template(
        'index.html', button_python=button_python, button_telegram=button_telegram, button_html=button_html, button_db=button_db
        )
class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
#Вывод объекта и id
    def __repr__(self):
        return f'<Card {self.id}>'

@app.route('/form_create', methods=['POST'])
def form_create():
        if request.method == 'POST':
            
            email =  request.form['email']
            text =  request.form['text']

        card = Card(text=text,email=email)
        db.session.add(card)
        db.session.commit()
        
if __name__ == "__main__":
    app.run(debug=True)