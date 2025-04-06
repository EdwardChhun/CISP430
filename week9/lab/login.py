
#  Laboratory 9 - Hash Table
#
# Program that reads in username/login pairs and then
# performs authentication of usernames until EOF is encountered
# or a successul login is acheived.


from HashTable import HashTable, Password

if __name__=="__main__":
    passwords=HashTable(10)
    tempPass = Password()


	#*********************************************************
	# Step 1: Read in the password file
	#*********************************************************
    passFile= open("password.txt",'r')

    if (not passFile):
        print("Unable to open 'password.txt'!")
    else:
        for line in passFile:
            uname,pwd=line.split()
            tempPass=Password(uname,pwd)
            passwords.put(tempPass)

    print(passwords)


	#*********************************************************
	# Step 2: Prompt for a Login and Password and check if valid
	#*********************************************************
    while True:  # to quit, type CTRL Z
        name=input( "Login: ")
        user = passwords.get(name)
        
        pwd=input("Password: ")

        if user and user.password == pwd:
            print("Authentication successful\n")
        else:
            print("Authentication unsucessful\n")
        