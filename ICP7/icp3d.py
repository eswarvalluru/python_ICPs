import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
lemmatization=open("lemmatize.txt","w")
lemmatizer=WordNetLemmatizer()

with open("lines.txt", "r") as f:
    data = f.readlines()
for line in data:
    sentence =line
    stokens=nltk.sent_tokenize(sentence)
    text=nltk.word_tokenize(sentence)
    # print(pstemmer.stem(text))
    for word in text:
        lemmatization.write(lemmatizer.lemmatize(word))
        lemmatization.write("\n")