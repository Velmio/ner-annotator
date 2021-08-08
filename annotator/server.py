#import nltk

import spacy

from flask import Flask, request
from flask_cors import cross_origin

#from nltk.tokenize.treebank import TreebankWordTokenizer, TreebankWordDetokenizer

app = Flask(__name__)


@app.route("/tokenize", methods=["POST"])
@cross_origin()
def tokenize():
    text = request.json["text"]
    nlp = spacy.blank("en")
    doc = nlp(text)
    return {'tokens':[(t.idx, t.idx+len(t.text), t.text) for t in doc]}


@app.route("/detokenize", methods=["POST"])
@cross_origin()
def detokenize():
    tokens = request.json["tokens"]
    return {"text": ' '.join(tokens)}


if __name__ == "__main__":
    app.run(port=5555, debug=True)
