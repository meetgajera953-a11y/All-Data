li =[]

def inputd():
    num =int(input("enter data for a 1d array : (seprated bt spaces)"))
    for i in range(num):
        el=int(input(f"enter the element no.{i+1}:"))
        li.append(el)

def datas():
    print("data summary : ")
    print("-total elements :",len(li))
    print("-total value:",min(li))
    print("-maximum value:",min(li))
    print("-sum of all value:",sum(li))
    print("-average value:",sum(li)/len(li))

    li = [li]
def fact(a=1):
    if a<=1:
        return 1
    return a*fact(a-1)

def threshold():
    num4=int(input("enter a threshold value to filter out data above this value : "))
    for i in li:
        if i>=num4:
            print(i)    

while True:
    print("welcome to the data analyzar and transformer program \n")

    print("main menu")
    print("1.input data")
    print("2.disply data summary (bulit in function)")
    print("3.calculate factorial (recursion)")
    print("4.filter data by threshold (lambda function)")
    print("5.sort data ")
    print("6.disply dataset")
    print("7.exit programe")

    choice =int(input("please enter your chooice : "))

    if choice ==1:
        inputd()
        print("data has been storted successfully :\n")

    elif choice ==2:
        datas()

    elif choice ==3:
        num3=int(input("enter a number tp calculate its factorial : "))
        result =fact(num3) 
        print(f"factorial of ",num3,"is :",result) 

    elif choice ==4:
        threshold()

    elif choice ==5:
        choice =int(input("choice sorting option: "))
        if choice==1:
            li.sort
            print("sorted data in ascending order: ")

        if choice==2:
            li.sort(reverse=True) 
            print("sorted data in decending order:",li) 

    elif choice==6:
        # multi()
        pass
    elif choice==7:
        print("thank you for using the data analyzar and transformer program.goodbye!")
        break

    else:
        print("thankyou")     
        