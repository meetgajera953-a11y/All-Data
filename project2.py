print("Welcome to the Pattern Generator and Number Analyzer ! ")
print()
print()

while True :
    print()
    print("Select an option :")
    print()
    print("1. Generate a pattern :")
    print("2. Analyze a Range of Number :")
    print("3. exit")
    print()

    choice = int(input("Enter your Choice :"))


    if choice == 1 :
       a = int(input("Enter the Number for the Pattern :"))
       print()
       print("pattern :")
       for i in range (1,a+1) :
           print("*"*i)
    
    elif choice == 2:
        n = int(input("Enter the start of The Range :"))
        n1 = int(input("Enter the end of The Range :"))
        n3 = 0

        for i in range(n,n1,+1) :
            if i%2==0:
                print("Number",i,"is Even")
                
            else :
                print("Number",i,"is odd")
                
            n3 += i
        print ("sum of all numbers from",n,"to",n1,"is :",n3)    
        

    elif choice == 3 :
        print("Exiting program. Goodbye !")
        break
    else :
        print("Invalid choice")

    


    

    
     





    

        
             
        
    
            

    
    

       
    




