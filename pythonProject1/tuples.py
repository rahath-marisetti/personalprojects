numbers = (1, 2, 3) #paranthesis to define a tuple
numbers.count(3)

#mytuple = ( "apple", "banana", "cherry")
#print(mytuple)
#print(len(mytuple)) #length of tuple

# tuple items
#tuple3= (True, False, False)#boolean
#print(tuple3)
#tuple2 = (1, 5, 7, 9, 3)#numbers
#print(tuple2)

#tuple1 = ("abc", 34, True, 40, "male")#can be mix
#print(tuple1)

#thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
#print(thistuple)

thistuple8 = ("s", "john", "kim")
if "sam" in thistuple8:
    print("sam is here")
else:
    print("end")

print(thistuple8.index("john"))#checks tuple for specific value

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

mytuple3 = ("sam", "kim", "john", "alex", "rick")
print(mytuple3[2:6])



