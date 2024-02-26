""" #Data types
#Numbers 1,2,3
def add (x,y):
    print(x + y)
add (1,2)

#strings "a, b, c"
name = "Mark"
def greeting(person):
    print(person)
greeting(name)
#1 and "1" are not the same
add("1","2")
#undefined/null

#booleans (true or false)
tenure=True
def is_tenured(status):
    if(status == True):
        print("They have tenure")
    else:
        print("They are not tenured") """

""" x = 3
y = float(3)
print(x,y) """

""" values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i) """

""" print(values[0])
print(values[6]) """

""" x = "this is a thing" #string
y= x.split( ) #split string
z = y[0] #z = first word of the split string
print(y)
print(z) """

""" sentence = input()
word = sentence.split()
print(len(word))
 """

""" day_of_week = input("what day is it?")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect") """

""" x = "test"
print(f"hello {x}") """

""" temp = 68
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """

""" n = input()
if n == '2':
    print('even')
elif n == "3":
    print('odd')
elif n == '4':
    print ('even')
elif n == '5':
    print('odd')
elif n == '6':
    print('even')
else:
    print ('no more') """




""" service = input("How was the service? Use words great, good, mid, or bad. Put here:")
if service == "great":
    print('25%')
elif service == "good":
    print('20%')
elif service == "mid":
    print('15%')
elif service == "bad":
    print('0%')
else:
    print('Dont pay the bill') """

""" factor1 = int(input("Put your 1st number here:"))
factor2 = int(input("Put your 2nd number here:"))

def gcf(x,y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1,smaller+1):
        if((x % i ==0)) and ((y % i ==0)):
            gcf = i
    return gcf


print("Factors of number 1: ".format(factor1))
for i in range(1, factor1+1):
    if(factor1 % i == 0 ):
        print(i)

print("Factors of number 2: ".format(factor2))
for i in range(1, factor2+1):
    if(factor2 % i == 0 ):
        print(i) 

print("Greatest Common Factor between your numbers:", gcf(factor1, factor2)) """

