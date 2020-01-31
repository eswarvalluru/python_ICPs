# n=input()
# sum=0.0
# for i in range(n):
#     x=int(input())
#     sum=sum+x
# print(sum/n)

# m="yes"
# sum=0.0
# n=0
# while m[0] is 'y':
#     x=int(input())
#     n+=1
#     sum+=x
#     m=input()
# print(sum/n)


# infile=open('input.txt','r')
# sum=0.0
# count=0
# line=infile.readline()
# while line!="":
#     sum=sum+int(line)
#     count+=1
#     line=infile.readline()
# print(sum/count)

infile=open('input.txt','r')
count=0
d=dict()
line=infile.readline()
while line!= "":
    for xStr in line.split():
        if xStr in d:
            d[xStr]+=1
        else:
            d[xStr]=1
    line = infile.readline()
for key in list(d.keys()):
    print(key,":", d[key])
outfile=open('output.txt','w')
outfile.write(str(d))
outfile.close()
# print(d)