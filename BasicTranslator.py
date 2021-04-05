def english():
    print("Good morning")

def german():
    print("Guten morgen")

def italian():
    print("Buongiorno")

def spanish():
    print("Buenos dias")

# Main
while True:    #This simulates a Do Loop
    print("Select a Language and I will say 'Good Morning': ")
    print("1. English")
    print("2. Italian")
    print("3. Spanish")
    print("4. German")
    print("5. End the Program")
    choice = int(input())
    while choice < 1 or choice > 5:
        print("Invalid input! Please enter your selection from 1-5: ")
        print("1. English")
        print("2. Italian")
        print("3. Spanish")
        print("4. German")
        print("5. End the Program")
        choice = int(input())
    if choice == 1:
        english()
    else:
        if choice == 2:
            italian()
        else:
            if choice == 3:
                spanish()
            else:
                if choice == 4:
                    german()
    if not(choice != 5): break   #Exit loop
print("You have chosen to end the program! Goodbye!")
