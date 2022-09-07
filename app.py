from tkinter.font import names
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    
    return render_template('home.html')

@app.route('/')
def home():
    teams = ['Giants','Falcons', 'Bills', 'Rams', 'Ravens']
    return render_template('favorite5.html', teams=teams)

