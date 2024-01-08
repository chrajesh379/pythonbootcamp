from random import randint
def if_elif_analysis():
    print("------------------------if analysis start--------------")
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
    print("------------------------if analysis End--------------")

def for_analysis():
    print("------------------------for analysis start--------------")

    l=[1,2,3,4,5,6,7,8,9,10]
    t=(1,2,3)
    d={"k1":"1","k2":"2","k3":"3"}
    l1=[(1,2),(3,4),(5,6)]
    for i in l:
        if i%2==0:
            print(f"Even Number {i}")
        else:
            print(f"Odd Number {i}")
    for i in t:
        print(i)
    for k,v in d.items():
        print(f"key is {k} and value is {v}")
    for a,b in l1:
        print(f"tuple is {a} and {b}")

    st = 'Print only the words that start with s in this sentence'
    for i in st.split(" "):
       if i.lower().startswith("s"):
           print(i)
    st1 = 'Print every word in this sentence that has an even number of letters'
    for i in st1.split(" "):
        if len(i)%2==0:
            print(i)


    print("------------------------for analysis End--------------")

def special_operators():
    print("------------------------special_operators start--------------")
    #range : range operator is generator
    #generaor: generates information instead of saving in memory
    for i in range(0,10,1):
        print(i)
    print(list(range(0,10,1)))

    # enumerate function takes any iteratable object and gives index and value
    s='abcde'
    for i,v in enumerate(s):
        print(f"i and v is {i}:{v}")

    l1=[1,2,3,4]
    l2=["a","b","c"]
    l3=["10","20","30"]
    print(list(zip(l1,l2,l3)))
    print("------------------------special_operators End--------------")

def list_comprehesion():
    print("---------------------------------------list_comprehesion---------------------")
    names = ['Ch', 'Dh', 'Eh', 'cb', 'Tb', 'Td']
    l = [x for x in names if x.lower().startswith("c")]
    print(l)

    l1 = [x for x in range(0,11) if x%2==0]
    print(l1)
    l2 = [x for x in range(1,51) if x%3==0]
    print(l2)

    l3 = [ "FizzBuzz" if i%3==0 and i%5==0 else "Fizz" if i%3==0 else "Buzz" if i%5==0 else i for i in range(1,100)]
    print(l3)

    st = 'Create a list of the first letters of every word in this string'
    x=[ i[0] for i in st.split(" ")]
    print(x)
    print("---------------------------------------list_comprehesion---------------------")

def while_analysis():
    print("---------------------while loop ---------------------------")
    print("---------------------Number Game ---------------------------")
    random_int = randint(1,100)
    guesses=[0]
    while True:
        input_value = abs(int(input("Enter the Player Guess range from 1 to 100:")))
        if input_value<1 and input_value>100:
            print("OUT OF BOUNDS")
            continue
        if input_value==random_int:
           print(f"Player guesses the number {input_value}")
           break

        guesses.append(input_value)
        print(guesses)

        if guesses[-2]:
            if abs(random_int-input_value)<abs(random_int-guesses[-2]):
                print("WARMER!")
            else:
                print("COLDER!")
        else:
            if abs(random_int-input_value)<= 10:
               print("WARM!")
            else:
               print("COLD!")



    print("---------------------Number Game ---------------------------")

    print("---------------------while loop ---------------------------")

if __name__ == "__main__":
    if_elif_analysis()
    for_analysis()
    special_operators()
    list_comprehesion()
    while_analysis()
