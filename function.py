# # Python is called by

# def testfunction(arg):
#    print ("Inside function:",arg)
#    print ("ID inside the function:", id(arg))
#    arg=arg.append(100)

# var=[10, 20, 30, 40]
# print ("ID before passing:", id(var))
# testfunction(var)
# print ("list after function call", var)
# print ("ID after passing:", id(var))

# # Parameters
# def add(x,y):
#    z=x+y
#    return z

# a=10
# b=20
# result = add(a,b)
# print ("a = {} b = {} a+b = {}".format(a, b, result))

# print('a'[:0])


# Key word argument
def name_(name, location):
    return f'{name} is from {location}'

# print(name_('Asum', location='Princeton, NJ, USA'))

# Keyword only


def name_2(name, *, location, age):
    return f'{name} is from {location}. Age is {age}'

# print(name_2('Asum', location='New Jersey, Princeton', age=45))


def myfunction(x, /, y, *, z):
    print(x, y, z)
    

def arbiraryPositional(*s,**params,):
    for i in s:
        print(i)
    for x, y in params.items():
        print(x,y, sep=',')
    

arbiraryPositional(10,11,1,1,1,3,1,x=2,y=3,s=4,f=5,g=5,h=43)


# myfunction(10, y=20, z=30)



