from flask import Flask, render_template
from service import Data
app = Flask(__name__)
data = Data()
@app.route('/')
def hello():
    return  str(data.r[0])
    #return render_template("home.html")
@app.route('/profile/<name>')
def profile(name=None):
    return render_template("profile.html", name=name)
if __name__ == '__main__':
    app.run("0.0.0.0", debug=True)