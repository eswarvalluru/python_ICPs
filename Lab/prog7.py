#Tokenization
import nltk
nltk.download('punkt')
f =open("input.txt","r")
w=""
w=f.read()
word_token=nltk.word_tokenize(w)
for i in word_token:
   print(i)


#Lemmatization
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
lem= WordNetLemmatizer()
for i in word_token:
   print(lem.lemmatize(i))


#TRIGRAM
from nltk.util import ngrams
trigrams=ngrams(word_token,3)
l=[]
for t in trigrams:
  l.append(t)
  print(t)


#getting the trigrams with frequency
wordFrequency = nltk.FreqDist(l)
Frequency_Trigrams = wordFrequency.most_common()
print("TRIGRAMS WITH FREQUENCY:\n",Frequency_Trigrams)


# Top 10 Trigrams.
ten = wordFrequency.most_common(10)
print("Top 10 Trigrams:\n",ten)

# Concatenating the results
sentence = nltk.sent_tokenize(w)
Result = []


# Iterating the Sentences
for s in sentence:
    # Iterating through each sentence
    for a, b, c in l:
        # iterating through top 10 trigrams
        for ((i, j, k), length) in wordFrequency.most_common(20):
            # iterating through all trigrams
            if (a, b, c == i, j, k):
                Result.append(s)

print("Final Result : \n", Result)