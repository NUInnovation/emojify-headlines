#Emojify: Automatic emoji translation
EECS 395: Design and Innovation in Journalism. Spring 2016

##Team Members
 - Diane Liu
 - Kaolin Mo
 - Dara Rubin
 - Chenhui Zhou

##Setup Instructions
####1. Flask Setup:
1. Make sure you have pip installed.

2. Install virtualenv
  ```
  sudo pip install virtualenv
  ```

3. Activate the `venv` virtual environment.
  ```
  virtualenv venv
  source venv/bin/activate
  ```

4. Install Flask
  ```
  pip install flask
  ```

5. Install NLTK
  ```
  pip install nltk
  ```

6. Download NLTK packages using `nltk-setup.py` script.
  ```
  python nltk-setup.py
  ```



####2. To start the app:
```
python app.py
```

  This should start the application on `localhost:5000`.

####3. To close out of the app and deactivate your virtual environment:
Close out of the application by typing `CTRL-C`

To deactivate your virtual environment:
```
deactivate
```

##To Dos
####Monday April 25, 2016
- change color of input text if word recognized
- synonym lookup/term expansion
- roots of words
- trim punctuation [DONE 04/25]
- capitalization - change everything to lowercase [DONE 04/25]
- handle negation
- word frequency


##Emojipedia API

Secured permission from Emojipedia to use their logo within Fair Use.

Secured API from Emojipedia:

https://docs.google.com/document/d/1ERR7q89jNkUA13AQUDqS96OWT25s80uekwhCfsmyw1s/edit?usp=sharing

Your private key:

ad591ab90c99dc4d632c35ee70d37c36341cb3ba