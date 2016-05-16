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
    lower = inputtext.lower()
    tokens = nltk.word_tokenize(lower)
    tags = nltk.pos_tag(tokens) 
    
    if print_statements:
      print "Tagged input:", tags, "\n"

    # translate each word individually
    antonym = False
    translation = ""
    for tag in tags:
      trans = ""

      word = tag[0]
      pos_tag = tag[1]

      if print_statements:
        print "Original word:", word
      
      if word == "not":
        if antonym == True:
          antonym = False
        else:
          antonym = True
        continue
      
      if antonym == True:
        word = find_antonym(word, pos_tag)
        antonym == False
      
      word = lemmatize(word, pos_tag)
      trans = dictionary_lookup(dictionary, word)

      if trans == "":
        syns = find_synonyms(word, pos_tag)
        for syn in syns:
          trans = dictionary_lookup(dictionary, syn)
          if trans != "":
            break

      translation += trans

    # render translation result
    return render_template('index.html', originaltext=inputtext, translation=translation)
  else:
    return render_template('index.html')

def load_dictionary():
  with open('emojis_lemmatized.json') as f:
    dictionary = json.load(f)
  return dictionary

def find_antonym(word, pos_tag):
  global print_statements

  tag = pos_tag[0:2]
  if tag != 'JJ':
    return word

  s = str(wn.lemma(word+".a.01."+word).antonyms())
  
  if print_statements:
    print "Found antonym:", s
  
  start = s.find("'")
  end = s.find(".")
  result = s[start+1:end]
  return result

def find_synonyms(word, pos_tag):
  global print_statements

  syns = []

  tag = get_wn_pos_tag(pos_tag)
  for synset in wn.synsets(word):
    for lemma in synset.lemmas():
      syns.append(lemma.name())

  if print_statements:
    print "Found synonyms", syns

  return syns

def get_wn_pos_tag(pos_tag):
  tag = pos_tag[0:2]

  if print_statements:
    print "Part of speech:", tag

  if tag == "VB":
    pos = wn.VERB
  elif tag == "JJ":
    pos = wn.ADJ
  elif tag == "RB":
    pos = wn.ADV
  elif tag == "NN":
    pos = wn.NOUN
  else:
    pos = False
  return pos

def lemmatize(word, pos_tag):
  global print_statements
  result = word

  pos = get_wn_pos_tag(pos_tag)

  # lemmatize word
  if pos:
    result = WordNetLemmatizer().lemmatize(word, pos)

  if print_statements:
    print "Lemmatized word:", result

  return result

def dictionary_lookup(dictionary, word):
  global print_statements
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

  if print_statements:
    print "Dictionary lookup:", word, result, "\n"

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
