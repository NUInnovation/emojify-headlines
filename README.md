#Emojify: Automatic emoji translation
EECS 395: Design and Innovation in Journalism. Spring 2016

##Team Members
 - Diane Liu
 - Kaolin Mo
 - Dara Rubin
 - Chenhui Zhou

##Setup Instructions
####1. Flask Setup
1. Make sure you have pip installed.
2. Set up virtualenv
```
sudo pip install virtualenv
```
3. activate the `venv` virtual environment.
```
cd venv
source bin/activate
```
4. install Flask
```
pip install flask
```

####2. To start the app:
```
python app.py
```

  This should start the application on `localhost:5000`.

##To Dos
####Monday April 25, 2016
- change color of input text if word recognized
- synonym lookup/term expansion
- roots of words
- trim punctuation
- capitalization - change everything to lowercase

##Emojipedia API

Secured permission from Emojipedia to use their logo within Fair Use.

Secured API from Emojipedia:

https://docs.google.com/document/d/1ERR7q89jNkUA13AQUDqS96OWT25s80uekwhCfsmyw1s/edit?usp=sharing

Your private key:

ad591ab90c99dc4d632c35ee70d37c36341cb3ba