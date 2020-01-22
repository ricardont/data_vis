from flask import Flask, render_template, jsonify
from service import Inegi
app = Flask(__name__)
@app.route('/')
def hello():
    return render_template("home.html")
@app.route('/poblacion/')
def poblacion():
    data = Inegi()
    return jsonify(data.poblacion) 
@app.route('/profile/<name>')    
def profile(name=None):
    return render_template("profile.html", name=name)
if __name__ == '__main__':
    app.run("0.0.0.0", debug=True)