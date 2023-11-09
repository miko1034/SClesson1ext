def question1():
    name = str(input("What is your name? "))
    print(f"Hello {name}")

def question2():
    name = str(input("What is your name? "))
    surname = str(input("What is your surname? "))
    print(f"Hello {name} {surname}")

def question3():
    print("What do you call a bear with no teeth?\nA gummy bear")    

def question4():
    a = int(input("First number: "))
    b = int(input("Second number"))
    print(f"The total is {a+b}")

def question5():
    a = int(input("First number: "))
    b = int(input("Second number"))
    c = int(input("third number"))
    print(f"The answer is {(a+b) & c}")

def question6():
    total = int(input("How many slices did you start with? "))
    eaten = int(input("How many slices have you eaten? "))
    newtotal = total - eaten
    if newtotal <= 0:
        print("Total is 0")
    else:
        print(f"Total is {newtotal}")

def question7():
    name = input("What is your name? ")
    age = int(input("What is your age? "))
    print(f"{name} next birthday you will be {age +1}")

#please i cant do more questions these are just too mind numbingly boring
#womp womp womp