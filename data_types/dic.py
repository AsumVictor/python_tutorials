numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
for x in numbers:
   print (x,":",numbers[x])
   
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
for x in numbers.keys():
   print (x)
   
x = 2.0001
print(x.is_integer())

for letter in 'Python':     # First Example
   if letter == 'h':
      break
   print ('Current Letter :', letter)
  
var = 10                    # Second Example
while var > 0:              
   print ('Current variable value :', var)
   var = var -1
   if var == 5:
      break

print ("Good bye!")


for letter in 'Python': # First Example
   if letter == 'h':
      continue
   print ('Current Letter :', letter)
var = 10 # Second Example
while var > 0:
   var = var -1
   if var == 5:
      continue
   print ('Current variable value :', var)
print ("Good bye!")