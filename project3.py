student = []

while True:

    print("\nWelcome to the Student Data Organiser !\n")

    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete student")
    print("5. Display Subject offered")
    print("6. Exit")

    choice=int(input("\nEnter Your choice :"))


    if choice==1:
        print("\nEnter student details :")
        st ={
            "id":int(input("student id :")),            
            "name":input("Name :"),            
            "age":int(input("Age :")),            
            "grade":input("Grade :"),            
            "Dob":input("Date of Birth (YYYY-MM-DD) :"),           
            "subject":input("Subject (comma - seprated) :")           
        }
        student.append(st)
        print("\nStudent added successfully!")

    elif choice==2:
        for st in student:
            print(f"Name :{st["name"]} | Age :{st["age"]} | Grade :{st["grade"]} | Date of Birth :{st["Dob"]} | Subjects :{st["subject"]}")

    elif choice==3:
        stid = int(input("\nEnter student ID to update :"))

        for st in student:
            if st["id"]==stid:
                st["name"]=input("Name :"),            
                st["age"]=int(input("Age :")),            
                st["grade"]=input("Grade :"),            
                st["Dob"]=input("Date of Birth (YYYY-MM-DD) :"),           
                st["subject"]=input("Subject (comma - seprated) :")

                print("student updated successfully !")


    elif choice==4:
        stid = int(input("\nEnter id to remove :"))
        
        for st in student :
              if st ["id"] == stid :
                   student.remove(st)
                   print("student successfully removed :")
              else :
                   print("student not found \n")

    elif choice==5:
        stid = int(input("\n Enter ID to show subject offere :"))
        for st in student:
            print(f"Subjects :{st["subject"]}")

    elif choice==6:
        print("Exiting")
        break

    else :
        print("invalid")
        








                
                

           





        


