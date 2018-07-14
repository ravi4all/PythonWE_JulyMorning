emailId = input("Enter EmailId : ")
pwd = input("Enter Password : ")

#=  - assignment Operator
#== - comparison operator
#AND/OR/NOT - Logical Operators

# AND - Both conditions must be true
##if emailId == 'ravi@gmail.com' and pwd == '12345':
##    print("Welcome")
##else:
##    print("Invalid input...")

# OR - Any one condition should be true
if (emailId == 'ravi@gmail.com') or (pwd == '12345'):
    print("Welcome")
else:
    print("Invalid input...")
