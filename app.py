from flask import Flask, request, render_template
import json
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
    trans = dictionary_lookup(dictionary, word)
    translation += trans

  # render translation result
  return render_template('index.html', originaltext=inputtext, translation=translation)

def load_dictionary():
  with open('emojis.json') as f:
    dictionary = json.load(f)
  return dictionary

def dictionary_lookup(dictionary, word):
  # strip whitespace and make lowercase
  word = word.rstrip(" !@#$%^&*()?.,").lower()
  result = ""
  result = unicode(result, 'utf-8')

  for key, value in dictionary.iteritems():
    if word == key:
      result = value["char"]
    else:
      if word in value["keywords"]:
        result = value['char']

  return result

if __name__ == '__main__':
  app.debug = True
  app.run()
