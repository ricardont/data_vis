#install virtual env
ssh```
sudo apt-get install python-virtualenv
pip install --index-url=https://pypi.python.org/simple/ flask
```
#Vagrant File
ssh```
    config.vm.network :forwarded_port, guest: 5000, host: 5000
```
#activate virtual env
ssh```
. venv/bin/activate
```
#main file
ssh```
if __name__ == '__main__':
    app.run("0.0.0.0", debug=True)
```
ssh```
#run app 
FLASK_APP=index.py
flask run --host=0.0.0.0
```

#versions
python 3.4
flask 1.1
