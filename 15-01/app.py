"""This is an application for a bank account """
#data = [[1,"Hitesh","Hit@1010"]]
#count = data[0][0]

def features(flag):
    #print(flag)
    print("Press 1 for Balance Enquiry")
    print("Press 2 for Money withdrawal")
    print("Press 3 to add money")
    f_a = int(input())
    if f_a == 1:
        print("Money in your account ",data[flag-1][3])
    elif f_a == 2 :
        rem = int(input("enter the amount you want to remove"))
        if (data[flag-1][3]-rem) >= 0:
            data[flag-1][3] = data[flag-1][3] - rem
            print("Money withdrawal")
            print("Remaning amount :",data[flag-1][3])
        else : 
            print("You dont have this much amount")
    elif f_a ==3:
        add = int(input("enter amount"))
        data[flag-1][3] = data[flag-1][3] + add

    

def login():
   #print(data)
    print("Welcome to our app")
    print("Enter your account number")
    a_num = int(input())
    
    i = count-1
    if a_num == data[i][0]:
        print("Welcome :",data[i][1])
        print("Enter password")
        a_pass = (input())
        if a_pass == data[i][2]:
            print("Successfull Logined".center(30,'-'))
            features(data[i][0])
            
        else :
            print("password incorrect")
    else:
        print("USER Name not exists")
            


def signup():
    print("Welcome to our signup portal")
    name = input("Enter your name: ")
    p = input('Enter a password (It must have one special character one upper number one lower number): ')
    if(not p.isupper() and not p.islower() and not p.isspace() and not p.isalpha() and not p.isdigit() and not p.isalnum() ):
        print("You are successfully signedup")
        data.append([count,name,p])
        print("your new Unique id is: ",data[count-1][0])
        print("your Name is: ",data[count-1][1])
        print("your Password is: ",data[count-1][2])
        print("Login again")
        login()
    else :
        print("Re-enter password")


data = [[1,"Hitesh","Hit@1010",2500]]
count = data[0][0]

print('Press 1 for login')
print('Press 2 to create an account')
print('Press 3 to exit')
num = int(input())
if num == 1 :
    login()
elif num == 2 :
    count+=1
    signup()
else:
    print("Thanks visit again")
