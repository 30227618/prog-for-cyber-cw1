"""Created a dictionary containing a username, ip, event type, and risk level"""
details = {
    "username": "admin",
    "ip": "192.168.10.1",
    "event_type": "Brute Force Login",
    "risk_level": "High"
}

def display_username_ip():  #Defines the function to display the username and ip address
    print(f"Username: {details["username"]}")   #Displays the username
    print(f"IP Address: {details["ip"]}")   #Displays the ip address

def add_new_field():    #Defines the function to add a new field called "Status" to the dictionary
    status = input("Enter status (Active or Inactive): ").strip()   #Asks the user to enter the status they want to add and stores it as status
    details["status"] = status  #Adds the status to the dictionary with the key "status" and the value of status
    print(f"Added status: {status}.") #Prints a message confirming that the status has been added to the dictionary

def update_risk_level():    #Defines the function to update the risk level in the dictionary
    new_risk = input("Enter the risk level you want it changed to: ").strip()   #Asks the user to enter the new risk level and stores it as new_risk
    details["risk_level"] = new_risk    #Updates the risk level in the dictionary with the key "risk_level" and the value of new_risk
    print(f"Risk level updated to: {new_risk}.")   #Prints a message confirming that the risk level has been updated in the dictionary

def remove_field(): #Defines the function to remove a field from the dictionary
    del_req = input("Enter the field name that you want to delete: ").strip().lower()   #Asks the user to enter the field name they want to delete and stores it as del_req
    if del_req in details:
        del details[del_req]    #Removes the field from the dictionary if it exists
        print(f"Removed {del_req}") #Prints a message confirming that the field has been removed from the dictionary
    else:
        print(f"{del_req} not found. Try again.")   #Prints a failure message if the field is not found

def display_all_fields():   #Defines the function to display all keys and values in the dictionary
    for key, value in details.items():  #Loops through each key-value pair in the dictionary
        print(f"{key}: {value}")    #Prints each key-value pair

def display_no_key_value_pairs():   #Defines the function to display the total number of key-value pairs in the dictionary
    print(f"There are {len(details)} key-value pairs.") #Prints the total number of key-value pairs in the dictionary

def main(): #Defines the main function
    while True:
        """Displays a menu and asks the user to select an option. Based on the selected option, it calls the corresponding function to perform the desired operation"""
        print("\n==========================")
        print("     SECURITY MANAGER")
        print("==========================")
        print("1. Display username and IP address")
        print("2. Add new field called 'Status'")
        print("3. Update risk level")
        print("4. Remove a field")
        print("5. Display all keys and values")
        print("6. Display total number of key-value pairs")
        print("7. Exit")
        
        choice = input("\nEnter your choice: ")    #Asks the user to select an option from the menu and stores it as choice
        match choice:   #Uses match-case statement to check the value of choice and call the corresponding function
            case "1":
                display_username_ip()   #Calls the function to display the username and ip address if the user picks 1
                input("\nPress Enter to continue...") #Asks the user to press Enter to continue
            case "2":
                add_new_field() #Calls the function to add a new field called "Status" to the dictionary if the user picks 2
                input("\nPress Enter to continue...")   #Asks the user to press Enter to continue
            case "3":
                update_risk_level() #Calls the function to update the risk level in the dictionary if the user picks 3
                input("\nPress Enter to continue...")   #Asks the user to press Enter to continue
            case "4":
                remove_field()  #Calls the function to remove a field from the dictionary if the user picks 4
                input("\nPress Enter to continue...")   #Asks the user to press Enter to continue
            case "5":
                display_all_fields()    #Calls the function to display all keys and values in the dictionary if the user picks 5
                input("\nPress Enter to continue...")   #Asks the user to press Enter to continue
            case "6":
                display_no_key_value_pairs()    #Calls the function to display the total number of key-value pairs in the dictionary if the user picks 6
                input("\nPress Enter to continue...")   #Asks the user to press Enter to continue
            case "7":
                break   #Exits the program if the user picks 7
            case _:
                print("Invalid choice. Enter a number from 1 - 7")  #Prints an error message if the user enters an invalid choice

if __name__ == "__main__":  #Checks if the script is being run directly
    main()