fname = input("Enter file name: ")
num_words = 0
d=dict()
with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)
        for i in words:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
for key in list(d.keys()):
    print(key, d[key])