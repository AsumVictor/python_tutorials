<<<<<<< HEAD

 a = int(3.163)
 print(a, type(a))

 b = int(True)
 print(b, type(b))
 

 c = float("10.5")
 print(c)

d = int("11100110", 2)
print(d)



x = str(10e5)
print(x)


print(  dict([[30,8],[40,89]]))



a = 'fsfw fewfew fewfewf '
print(eval('a'))



a = 20            
b = 10            

print ('a=',a,':',bin(a),'b=',b,':',bin(b))
c = 0

c = a & b;        
print ("result of AND is ", c,':',bin(c))

c = a | b;     
print ("result of OR is ", c,':',bin(c))

c = a ^ b;        
print ("result of EXOR is ", c,':',bin(c))

c = ~a;           
print ("result of COMPLEMENT is ", c,':',bin(c))

c = a << 2;       
print ("result of LEFT SHIFT is ", c,':',bin(c))

c = a >> 2;       
print ("result of RIGHT SHIFT is ", c,':',bin(c))
=======
# Intergers
integer = 2
float = 2.59

class User: 
  def __init__(this, user_name, password): 
    this.name = user_name
    this.password = password

def __str__(this):
  return f"The name is {this.name} and the password is {this.password[:3] + '******'}"
>>>>>>> f4bbaeebf6fd6ce00ab159257dab47f4d671e55e
