import datetime
import time
import math
import random
import uuid
import importlib
import project62 as p62

while True:
    print("""
        ===========================
        Welcome to Multi-Utility Toolkit
        ===========================
        Choose an option:
        1. Datetime and Time Operations
        2. Mathematical Operations
        3. Random Data Generation
        4. Generate Unique Identifiers (UUID)
        5. File Operations (Custom Module)
        6. Explore Module Attributes (dir())
        7. Exit
        ===========================
          """)
    try:
        mainchoice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Please enter a valid integer choice.")
        continue

    if mainchoice == 7:
        print("""
            ===========================
            Thank you for using the Multi-Utility Toolkit!
            ===========================""")
        break

    elif mainchoice == 1:
        while True:
            print("""
                Datetime and Time Operations:
                1. Display current date and time
                2. Calculate difference between two dates/times
                3. Format date into custom format
                4. Countdown Timer
                5. Back to Main Menu
                  """)
            try:
                subchoice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input! Please enter a valid integer choice.")
                continue

            if subchoice == 5:
                break
            elif subchoice == 1:
                current = datetime.datetime.now()
                print("Current Date = ", current.date())
                print("Current Time = ", current.time())
                print("=============================")
            elif subchoice == 2:
                f = input("Enter First Date (YYYY-MM-DD): ")
                s = input("Enter Second Date (YYYY-MM-DD): ")
                try:
                    fy, fm, fd = map(int, f.split("-"))
                    sy, sm, sd = map(int, s.split("-"))
                    fdate = datetime.date(fy, fm, fd)
                    sdate = datetime.date(sy, sm, sd)
                    dif = sdate - fdate
                    print("Difference:", dif)
                except Exception as e:
                    print("Error in date input:", e)
                print("=============================")
            elif subchoice == 3:
                aa = datetime.datetime.now()
                formateddate = aa.strftime("%Y--%m--%d")
                print(f"The Custom Date is: {formateddate}")
                print("=============================")
            elif subchoice == 4:
                try:
                    timer = int(input("Enter your time for timer in seconds: "))
                    if timer < 0:
                        print("Please enter a positive integer for time.")
                        continue
                except ValueError:
                    print("Invalid input! Please enter a valid integer.")
                    continue
                print(f"Your Timer is Set for {timer} Seconds")
                time.sleep(timer)
                print("\nTime UP, Time UP !!")
                print("=============================")
            else:
                print("====Enter Valid Choice====")

    elif mainchoice == 2:
        while True:
            print("""
                Mathematical Operations:
                1. Calculate Factorial
                2. Solve Compound Interest
                3. Back to Main Menu
                  """)
            try:
                subchoice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input! Please enter a valid integer choice.")
                continue
            if subchoice == 3:
                break
            elif subchoice == 1:
                try:
                    fac = int(input("Enter number to calculate Factorial: "))
                    if fac < 0:
                        print("Factorial is not defined for negative numbers.")
                        continue
                except ValueError:
                    print("Invalid input! Please enter a valid non-negative integer.")
                    continue
                factorial = math.factorial(fac)
                print(f"The factorial of number {fac} is {factorial}")
                print("=============================")
            elif subchoice == 2:
                try:
                    pamount = float(input("Enter Principal Amount: "))
                    rrate = float(input("Enter Rate of Interest (in %): "))
                    per = float(input("Enter Time (in years): "))
                    if pamount < 0 or rrate < 0 or per < 0:
                        print("Please enter non-negative values only.")
                        continue
                except ValueError:
                    print("Invalid input! Please enter numeric values.")
                    continue
                r = rrate / 100
                amount = pamount * (1 + r) ** per
                print(f"The Final Amount at End of Year is = {amount:.2f}")
                print("=============================")
            else:
                print("====Enter Valid Choice====")

    elif mainchoice == 3:
        while True:
            print("""
                Random Data Generation
                1. Generate Random Number
                2. Generate Random List
                3. Generate Random OTP
                4. Back to Main Menu
                  """)
            try:
                subchoice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input! Please enter a valid integer choice.")
                continue
            if subchoice == 4:
                break
            elif subchoice == 1:
                print(f"The random number generated is = {random.random() * 10}")
                print("=============================")
            elif subchoice == 2:
                l = []
                for i in range(1, 6):
                    aa = random.randint(1, 100)
                    l.append(aa)
                print(f"The list of random numbers is: {l}")
                print("=============================")
            elif subchoice == 3:
                aa = str(random.randint(10, 100))
                ab = str(random.randint(10, 100))
                print(f"The Random OTP is: {aa + ab}")
                print("=============================")
            else:
                print("====Enter Valid Choice====")

    elif mainchoice == 4:
        print(f"\nGenerated UUID: {uuid.uuid4()}")
        print("=============================")

    elif mainchoice == 5:
        print("Launching Journal Manager (File Operations)...")
        p62.run_journal_manager_menu()
        print("=============================")

    elif mainchoice == 6:
        explore = input("Enter module name to explore: ")
        try:
            mod = importlib.import_module(explore)
            print(f"Available attributes in {explore} are:")
            print(dir(mod))
        except ModuleNotFoundError:
            print(f"Module '{explore}' not found.")
        print("=============================")

    else:
        print("====Enter Valid Choice====")
