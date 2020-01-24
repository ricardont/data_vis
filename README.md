## install virtual env
```ssh
 sudo apt-get install python-virtualenv 
 pip install --index-url=https://pypi.python.org/simple/ flask  
```
## Vagrant File
```ssh
    config.vm.network :forwarded_port, guest: 5000, host: 5000
```
## create  virtual env
```ssh
 virtualenv --python=/usr/bin/python3.6 venv --always-copy
```
## activate virtual env
```ssh
. venv/bin/activate
```
## deactivate virtual env
```ssh
deactivate
```
## main file
```py
if __name__ == '__main__':
    app.run("0.0.0.0", debug=True)
```
## run app 
```py
FLASK_APP=index.py
flask run --host=0.0.0.0
```
## Git set proxy
```ssh
git config --global http.proxy http://proxyuser:proxypwd@proxy.server.com:8080
```
## Git unset  proxy
```ssh
git config --global --unset http.proxy
git config --global --get http.proxy
```
## versions
+ python 3.4
+ flask 1.1

