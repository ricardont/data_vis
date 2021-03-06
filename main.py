from flask import Flask, render_template, jsonify
from services import Corona, Inegi
app = Flask(__name__)
@app.route('/')
def hello():
    data = Corona()
    return render_template("home.html", data=data)
@app.route('/population/')
def population():
    data = Inegi()
    djson = jsonify(data.population) 
    return render_template("grid.html", data=data.population)    
@app.route('/profile/<name>')    
def profile(name=None):
    return render_template("profile.html", name=name)
if __name__ == '__main__':
    app.run(debug=True)