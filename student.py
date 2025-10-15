students = []

while True :

    print("\nWelcome to our Programme :")

    print("1. add")
    print("2. read")
    print("3. delete")
    print("4. update")
    print("5. exit")

    choice = int(input("enter your choice :"))
    
    if choice==1:
          st = { 
            "stid":int(input("Enter student stid :")),
            "name": input("Enter student Name :"),
            "city" : input("Enter student City :")
            
            }
          students.append(st)
          print("student added successfully !")

    elif choice == 2 :
         for st in students :
              print("name :", st["name"], "city", st["city"])
              

    elif choice == 3 :
         stid = int(input("enter student id to remove :"))

         for st in students :
              if st ["stid"] == stid :
                   students.remove(st)
                   print("student successfully removed :")
              else :
                   print("student not found \n")
            
    elif choice == 4 :
        stid = int(input("enter student id to update :"))

        for st in students :
            if st["stid"] == stid:
                st["name"] = input("enter the new name :")
                st["city"] = input("enter the new city :")
                print("student successfully updated :")
                print()
               

    elif choice == 5 :
         print("eciting")
         break
    
    else :
         print("invalid")
         
        
    



