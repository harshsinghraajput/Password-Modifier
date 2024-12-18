SECURE = (('A','/|'),('a','@'),('b','6'),('C','['),('K','|<'),('L','|_'),('O','()'),('S','&'),('s','$'))

def passwordsecure(password):
    for a,b in SECURE:
        password = password.replace(a,b)

    return password

password = input("Please enter your password for modification : ")
decision = input("Do you need Upper Case letters to be present? (y/n) ")

if decision == 'y' or 'yes':
    print(f"Your new Modified Password is {passwordsecure(password)}")
else:
    print(f"Your new password with all lower case letters is {passwordsecure(password)}")

    