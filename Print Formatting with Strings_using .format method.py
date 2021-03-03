
#to format the objects in the string using .format method:

print('The {}'.format('fox'))

print('The {} {} {}{}' .format('fox','is','brown','.'))

#to shift the index position of objects in the string using .format method:

print('The {2} {0}' .format('fox','is','brown','.'))

#to repeat the index position of an object within the string
print('The {0} {0}' .format('fox', 'is','brown','.'))


#to use keywords as variable names in .format method to format objects in the string

print('The {f} {i} {b}' .format(f='fox',i='is',b='brown'))

print('The {f} {f} {f}' .format(f='fox',i='is',b='brown'))

#float formatting using .format method: "value:width.precision f)"
#width=size of the sting of numbers=number of digits in a number string
#value=the number/result value you want to apply this formatting method
#precision=how long after decimal you want your value/number figure

#Let's say

result=100/777
result
print ("the result was {}".format('0.1287001287001287'))

print("the result was {r}" .format(r=result))

#now we will use float formatting using .format method: "value:width.precision f)"

print("the result was {r:1.3f}" .format(r=result))

#to extend the length of number string, we will increase the width as done below:

print("the result was {r:10.3f}" .format(r=result))

#Lets say

result=104.12345
print("the result was {r:1.3f}" .format(r=result))

print("the result was {r:10.3f}" .format(r=result))

