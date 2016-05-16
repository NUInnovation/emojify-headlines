import json
import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet as wn

def lemmatize(word, pos_tag):
  tag = pos_tag[0:2]

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

def get_new_lemmas(word, lemmas):
  tokens = nltk.word_tokenize(word)
  tags = get_pos(tokens)
  for tag in tags:
    lm = lemmatize(tag[0], tag[1])
    if lm != tag[0]:
      lemmas.append(lm)

def get_pos(word):
  return nltk.pos_tag(word)

def load_dictionary():
  with open('emojis.json') as f:
    dictionary = json.load(f)
  return dictionary

def main():
  dictionary = load_dictionary()
  for key, value in dictionary.iteritems():
    lemmas = []
    get_new_lemmas(key, lemmas)
    for word in value["keywords"]:
      get_new_lemmas(word, lemmas)
    if len(lemmas) > 0:
      print key, lemmas
      dictionary[key]["keywords"] += lemmas

  with open("emojis_lemmatized.json", "w") as wf:
    data = json.dumps(dictionary, ensure_ascii=False, indent=2, sort_keys=True).encode('utf-8')
    wf.write(data)
    #json.dump(dictionary, wf, sort_keys=True, indent=2, ensure_ascii=False, encoding="utf-8")

if __name__ == "__main__":
  main()
