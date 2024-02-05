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

values = [1,2.23,5,7,2,30,15]
""" print(values)
for i in values:
    print(i) """

""" print(values[0])
print(values[6]) """

""" x = "this is a thing" #string
y= x.split( ) #split string
z = y[0] #z = first word of the split string
print(y)
print(z) """

sentence = input("I like pizza, and ice cream")
for i in sentence:
    print(i)
    y=i.split()
    words_list = y(",")
print(len(words_list))
  