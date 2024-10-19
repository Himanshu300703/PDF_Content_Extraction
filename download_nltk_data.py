import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

text = "Hello! How are you? I hope you're doing well."
sentences = sent_tokenize(text)
print(sentences)
