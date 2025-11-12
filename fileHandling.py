while True :

    print(f"""\n Create your own File :\n
          1. press "x" to create new File : 
          2. press "R" to read created file File :
          3. press "w" to read write data in file File :
          4. press "a" to add new data in file File :
          5. press "e" to exit :""")
    
    choice = input("\nEnter your choice :")


    if choice =="x":
        file_name = input("enter your file name L:")

        with open(file_name , "x") as file :
            print(f"file {file_name} created successfully !")

    elif choice=="R":
        file_name = input("Enter File name to Read :")

        with open(file_name,"r") as file :
            print("\n your content -------")
            print(file.read())


    elif choice=="w":
        file_name = input("Enter data in file")

        with open(file_name, "w") as file:
            data = input("\nEnter data to your file :\n")
            file.write(data)

    elif choice=="a":
        file_name = input("Enter file name to append :")

        with open(file_name,"a") as file:
            data2=input("Enter data to add in oyur exixting file")
            file.write("\n"+ data2)

    elif choice=="e":
        print("exiting program :")
        break

    else:
        print("invalid")
        
       






    

    

