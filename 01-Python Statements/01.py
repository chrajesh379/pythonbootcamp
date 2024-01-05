
def if_elif_analysis():
    name = input("Please Enter your Name :")
    password = input("Please Enter your Password :")
    email = input("Please enter your email id :")

    if name.strip() =='':
        print("Name is invalid")
    else:
        if len(password)<8:
            print("Password Length Should be more then 8 ")
        else:
            if '@' not in email:
                print("Invalid Email")
            else:
                print("Success")

if __name__ == "__main__":
    if_elif_analysis()
