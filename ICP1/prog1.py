print('Enter Input String:')
a=list(input())
#print(a)
print("Enter the index of elements to be removed:")
index=input().split()
for i in range(len(index)):
    a.pop(int(index[i]))
a=a[::-1]
r=''.join(a)
print('The final result is:',r)