from flask import Flask, request, render_template
import optparse
import os
import json
import nltk
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
app = Flask(__name__)


@app.route('/')
def hello_world():
  return render_template('index.html')

@app.route('/translate', methods=['POST', 'GET'])
def translate():
  if request.method == 'POST':
    global print_statements

    # get input text from form
    inputtext = request.form['inputtext']

    # load dictionary JSON object
    dictionary = load_dictionary()

    # tokenize input sentence and POS tag
    inputtext = inputtext.lower()
    tokens = nltk.word_tokenize(inputtext)
    tags = nltk.pos_tag(tokens) 
    if print_statements:
      print tags

    # translate each word individually
    translation = ""
    for tag in tags:
      if print_statements:
        print tag[0]
      word = lemmatize(tag[0], tag[1])
      trans = dictionary_lookup(dictionary, word)
      translation += trans

    # render translation result
    return render_template('index.html', originaltext=inputtext, translation=translation)
  else:
    return render_template('index.html')

def load_dictionary():
  with open('emojis.json') as f:
    dictionary = json.load(f)
  return dictionary

def lemmatize(word, pos_tag):
  global print_statements

  # get part of speech of word
  tag = pos_tag[0:2]

  if print_statements:
    print tag

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

  if print_statements:
    print result

  return result

def dictionary_lookup(dictionary, word):
  # strip whitespace and make lowercase
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

  global print_statements
  if print_statements:
    print result

  return result

if __name__ == '__main__':
  nltk.data.path.append('./nltk_data/')

  parser = optparse.OptionParser()
  parser.add_option("--print", action="store_true", dest="print_statements")
  options, _ = parser.parse_args()

  global print_statements
  print_statements = options.print_statements

  app.debug = True
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port)
