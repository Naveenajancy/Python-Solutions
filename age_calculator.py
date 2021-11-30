print ("Hello user")
name = input("How old are you\n")
print(type(name))
age =str ( int(name)/10).split('.')
#print(age)
output = "you are "+ age[0] + "decades and "+age[1] + "Year old"
print (output)