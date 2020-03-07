import nltk
from nltk.stem import PorterStemmer
stemming=open("stem.txt","w")

with open("lines.txt", "r") as f:
    data = f.readlines()
for line in data:
    sentence =line
    stokens=nltk.sent_tokenize(sentence)
    text=nltk.word_tokenize(sentence)
    pstemmer=PorterStemmer()
    # print(pstemmer.stem(text))
    for word in text:
        stemming.write(pstemmer.stem(word))
        stemming.write("\n")