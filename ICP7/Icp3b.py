import nltk
nltk.download('averaged_perceptron_tagger')
partsofspeech=open("pos.txt","w")

with open("lines.txt", "r") as f:
    data = f.readlines()
for line in data:
    sentence =line
    stokens=nltk.sent_tokenize(sentence)
    text=nltk.word_tokenize(sentence)
    tagged=nltk.pos_tag(text)
    print(tagged)
    partsofspeech.write(str(tagged))
    partsofspeech.write("\n")