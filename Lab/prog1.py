import itertools
a=list(map(int,input().split()))
l=len(a)
for i in range(1,l+1):
    print(list(set(itertools.combinations(a,i))))
