from flask import Flask, render_template, jsonify
from service import Inegi
app = Flask(__name__)
@app.route('/')
def hello():
    return render_template("home.html")
@app.route('/population/')
def population():
    data = Inegi()
    djson = jsonify(data.population) 
    return render_template("grid.html", data=data.population)    
@app.route('/profile/<name>')    
def profile(name=None):
    return render_template("profile.html", name=name)
if __name__ == '__main__':
    app.run("0.0.0.0", debug=True)