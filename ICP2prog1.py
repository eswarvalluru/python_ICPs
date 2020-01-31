def listsc():
    print("Using List Comprehensions")
    print("Enter the Weights in lbs:")
    a=input().split()
    e=[round((int(c)/2.2),2) for c in a]
    print("Weights in kgs:")
    print(e)
    return 0

def loops():
    print("Using Loops")
    print("Enter the weights in lbs:")
    a=input().split()
    b=[]
    for i in a:
        b.append(round((int(i)/2.2),2))
    print("Weights in Kgs:")
    print(b)
    return 0

if __name__ =='__main__':
    a=input("Enter 1 for listcomprehensions 2 for loops:\n")
    if a is '1':
        listsc()
    else:
        loops()