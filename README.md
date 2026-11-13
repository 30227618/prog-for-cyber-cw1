# Security Tool

Programming for Cyber Security: Coursework 1, Task 1

## Student Details

| | |
|---|---|
| **Name** | Mohammed Ahmed |
| **Campus** | New College - Motherwell |
| **Banner ID** | B01886625 |

## Program Specifications

The program first authenticates the user. If the credentials are correct, the user is granted access to the rest of the program. 

After the user is granted access, they are presented with four options, which are:

1. **Security Event Counter**: The user is asked to enter a password 10 times. At the end, the number of times the correct and incorrect passwords were entered is displayed, along with the percentage of incorrect passwords entered. If the percentage is greater than 50%, then it raises an alert.
2. **Brute-Force Simulation**: Asks the user for a password and keeps asking until either the user enters it correctly or has had more than 10 attempts. Displays the number of attempts.
3. **Login Authentication**: Asks the user for username and password and allows three attempts. If failed attempts arre more than 3, displays message saying that the account has been frozen.
4. **Exit**: Exits the program.

## Testing
### Valid Input

![alt text](image-2.png)

### Invalid Input

![alt text](image-3.png)