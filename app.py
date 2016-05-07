from flask import Flask, request, render_template
import os
import json
import nltk
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
app = Flask(__name__)

@app.route('/')
def hello_world():
  return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
  # get input text from form
  inputtext = request.form['inputtext']

  # load dictionary JSON object
  dictionary = load_dictionary()

  # translate each word individually
  translation = ""
  for word in inputtext.split():
    word = lemmatize(word)
    trans = dictionary_lookup(dictionary, word)
    translation += trans

  # render translation result
  return render_template('index.html', originaltext=inputtext, translation=translation)

def load_dictionary():
  with open('emojis.json') as f:
    dictionary = json.load(f)
  return dictionary

def lemmatize(word):
  # get part of speech of word
  tagged = nltk.pos_tag([word])
  tag = tagged[0][1][0:2]

  if tag == "VB":
    pos = wn.VERB
  elif tag == "JJ":
    pos = wn.ADJ
  elif tag == "RB":
    pos = wn.ADV
  else:
    pos = wn.NOUN

  # lemmatize word
  result = WordNetLemmatizer().lemmatize(word, pos)

  return result

def dictionary_lookup(dictionary, word):
  # strip whitespace and make lowercase
  word = word.rstrip(" !@#$%^&*()?.,").lower()
  result = ""
  result = unicode(result, 'utf-8')

  for key, value in dictionary.iteritems():
    if word == key:
      result = value["char"]
      break
    
  if result == "":
    for key, value in dictionary.iteritems():
      if word in value["keywords"]:
        result = value["char"]

  if result == None:
    result = ""

  return result

if __name__ == '__main__':
  nltk.data.path.append('./nltk_data/')
  app.debug = True
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port)
