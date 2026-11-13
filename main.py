import security_tools   #Imports the security_tools module

password = input("Enter a password: ").strip()  #Asks user for a password
ip_address = input("Enter an IP address: ").strip() #Asks user for an IP address

if security_tools.validate_password(password) == True:  
    print("Password is valid.") #Prints success message if the password is valid
else:
    print("Password is invalid.")   #Prints error message if the password is invalid
    new_password = security_tools.generate_strong_password()    #Generates a strong password using the generate_strong_password function
    print(f"Suggested strong password: {new_password}") #Prints the suggested strong password

if security_tools.validate_ip(ip_address) == True:
    print("IP address is valid.")   #Prints success message if the IP address is valid
else:
    print("IP address is invalid.") #Prints error message if the IP address is invalid