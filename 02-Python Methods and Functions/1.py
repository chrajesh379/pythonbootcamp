

def check_even_list(l):
    # pleceholder to retunn
    even_list = []
    for num in l:
        if num%2==0:
            even_list.append(num)
    return even_list
def tuple_unpacking(t):
    max_sal=0
    emp_name=''
    for name,sal in t:
        if sal>max_sal:
            max_sal=sal
            emp_name=name
        else:
            pass
    return (emp_name,max_sal)
def function_analyis():
    print("------------------------function analyis---------------")
    print(check_even_list([1,2,3,4,6,7,8]))
    print(check_even_list([1,3]))
    print(tuple_unpacking([('Pattit',100),('Jeeny',200),('Blair',500),('lucas',100)]))
    print("------------------------function analyis---------------")

def args_kwargs(*args,**kwargs):
    print("-----------------------args and kwagrs--------------------")
    total=0
    for k,v in kwargs.items():
        print(f"key is {k} and {v}")
        total +=v
    print(f"total fruits are {total}")
    print(f"addiotion of number are {sum(args)}")

    print("-----------------------args and kwagrs--------------------")

def lesser_of_two_evens(a,b):
    print("---------------------lesser_of_two_evens----------")

    if a%2==0 and b%2==0:
        print(min(a,b))
    else:
        print(max(a,b))

    print("---------------------lesser_of_two_evens----------")

def animal_crackers(s):
    s=s.lower()
    if len(s.split())<=2:
        if s.split()[0][0]==s.split()[1][0]:
            print(f"First letters are matched { s.split()[0][0]} and {s.split()[1][0]}")
        else:
            print(f"First letters are not matched { s.split()[0][0]} and {s.split()[1][0]}")
    else:
        print(f"string length is greanthen two: {s}")

def makes_twenty(a,b):
    if a+b==20 or a==20 or b==20:
        return True
    else:
        return False

def old_macdonald(s_string,positions):
    positions=list(positions)
    #e_list=[]
    e_list=[s.upper() if idx in positions else s for idx,s in enumerate(s_string)]
    return "".join(e_list)

def master_yoda(s):
    word_list=s.split(" ")
    reversed_word_list=word_list[::-1]
    return " ".join(reversed_word_list)

def has_33(v_list):
    print("------------has_33------------")
    for i in range(0,len(v_list)-1):
        if v_list[i]==3 and v_list[i+1]==3:return True
    return False
    print("------------has_33------------")

def paper_doll(s,repeat):
    print("------------paper_doll------------")
    empty_str=''
    for i in s:
        empty_str +=i*repeat
    return empty_str
    print("------------paper_doll------------")

def blackjack(a,b,c):
    print("------------blackjack------------")
    l=[a,b,c]
    #print(sum(list([a,b,c])))
    if sum(l)<=21: return sum(l)
    elif sum(l)>=21 and 11 in l: return sum(l)-10
    else: return "BURST"
    print("------------blackjack------------")

def summer_69(l):
    print("------------summer_69------------")
    x=[]
    for i in l:
        if 6==i or 7==i or 8==i or 9==i:
            pass
        else:
            x.append((i))
    #print(l)
    return sum(x)
    print("------------summer_69------------")

def spy_game(l):
    x=[]
    for i in l:
        if i==0 or i==7:
            x.append(i)
    return x==[0,0,7]

def count_primenumbers(n):
    x=[]
    prime =True
    for i in range(2,n+1):
        for j in range(2,i):
            print(f"i and j are {i} {j}")
            if i%j==0:
                print(f"i and j are {i} {j} -- break")
                break
        else:
            x.append(i)
    return x,len(x)

def rotate_chr(c):
    rotate=3
    c=c.lower()
    alphabet='abcdefghijklmnopqrstruwxyz'
    # Keep punctuation and whitespace
    if c not in alphabet:
        return c
    rotate_pos=ord(c)+rotate
    # If the rotation is inside the alphabet
    if rotate_pos<=ord(alphabet[-1]):
        return chr(rotate_pos)
    # If the rotation goes beyond the alphabet
    return chr(rotate_pos-len(alphabet))

def map_analysis():
    #map(function, iterable[, iterable1, iterable2,..., iterableN])
    print(list(map(lambda n : n*n ,[1,2,3,4,5])))
    words = ["Welcome", "to", "Real", "Python"]
    # Length of each word
    print(list(map(len,words)))
    numbers = [-2, -1, 0, 1, 2]
    print(list(map(abs,numbers)))
    print(list(map(pow,[1,2,3],[2,2,3])))
    print(list(map(lambda x,y,z: x+y+z ,[1,2,3],[4,5,6],[7,8,9])))
    string_it = ["processing", "strings", "with", "map"]
    print(list(map(str.capitalize,string_it)))
    print("".join(map(rotate_chr, "My secret message goes here.")))


if __name__ == "__main__":
    function_analyis()
    args_kwargs(10,20,30,orange = 5,banana = 10,apple = 6)
    lesser_of_two_evens(2,4)
    lesser_of_two_evens(2,5)
    animal_crackers("Levelheaded Llama")
    animal_crackers("Levelheaded ama")
    animal_crackers("Levelheaded ama abcv")
    print(makes_twenty(20, 10))
    print(makes_twenty(17, 5))
    print(makes_twenty(10, 10))
    print(old_macdonald("macdonald",[0,3]))
    print(master_yoda('I am home'))
    print(has_33([1, 3, 3]))
    print(has_33([1, 3, 1, 3]))
    print(paper_doll('Hello',3))
    print(blackjack(1,10,1))
    print(blackjack(10, 10, 11))
    print(blackjack(8, 10, 9))
    print(summer_69([1, 3, 5]))
    print(summer_69([4, 5, 6, 7, 8, 9]))
    print(summer_69([2, 1, 6, 9, 11]))
    print(spy_game([1,2,4,0,0,7,5]))
    print(spy_game([1,0,2,4,0,5,7]))
    print(spy_game([1,7,2,0,4,5,0]))
    numbers,count=count_primenumbers(10)
    print(numbers)
    print(count)
    numbers,count=count_primenumbers(100)
    print(numbers)
    print(count)
    map_analysis()
