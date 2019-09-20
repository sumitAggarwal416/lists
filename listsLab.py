'''
I, Sumit Aggarwal, student number:000793607, certify that all code submitted is
my own code, that I have not copied it from any other source. I also certify
that I have not allowed anyone else to copy my code.
'''

def oneDlist():
    word= input("Enter any string ")
    list1=[word.title()]
    while word.capitalize()!='Quit':
        word=input("Enter another string ")
        list1.append(word.title())
        list1.sort()
    else:
        list1.remove("Quit")
    print(list1)
    for i in range(len(list1)):
        print(list1[i])
        i+=1


def twoDlist():
    number= int(input("Enter any number between [3,9]: "))
    while number<=2 or number>=10:
        print("The number is not in the specified range, try again")
        number= int(input("Enter any number between [3,9]: "))
    else:
        col=[]
        for c in range(number+1):
            row=[]
            for r in range(number+1):
                product=c*r
                row.append(product)
            col.append(row)

    print(col)
    print(" ")
    for c in range(number+1):
        print(col[c])
  
oneDlist()
twoDlist()
