def string_alternative(inp):
    r = ""
    for i in range(len(inp)):
        if i % 2 is 0:
            r += inp[i]
    return r
if __name__ == '__main__':
    s=input("Enter the input string:")
    result=string_alternative(s)
    print(result)
