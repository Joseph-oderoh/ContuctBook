from contact import *
from menu import *




def main():
    while True:
        display_menu()
        choice = input("Choose an option 1--4: ")
        if choice == "1":
            add_contact()
        elif  choice == "2":
            veiw_contact()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            print("See you next time!")
            break   
        else:
            print("Invalid input try")
              
main()              