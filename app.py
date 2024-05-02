#імпортує клас Flask з бібліотеки Flask. Це необхідно для створення екземпляру додатку Flask
from flask import Flask, render_template 

#створення екземпляру класу Flask
app = Flask(__name__)

# Це декоратор маршруту. Вказує, що функція, яка слідує після цього декоратора 
#буде викликатися, коли користувач запитує URL-адресу "/", тобто головну сторінку.
@app.route("/")
#функція яка буде повертати текст на головню сторінку
def hello_world():
    return render_template("index.html",)
#функція яка буде повертати текст на сторінку
@app.route("/contact/")
def contacts():
    return render_template("contact.html")
