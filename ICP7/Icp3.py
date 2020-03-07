import nltk
nltk.download('punkt')
lines = open("lines.txt", "w")
words= open("words.txt","w")

with open("data.txt", "r") as f:
    data = f.readlines()
for line in data:
    sentence =line
    stokens=nltk.sent_tokenize(sentence)
    wtokens=nltk.word_tokenize(sentence)
    for s in stokens:
        print (s)
        lines.write(s)
        lines.write("\n")
    for w in wtokens:
        print(w)
        words.write(w)
        words.write("\n")