str = "Hello,world!"
#print string
print(str)
#print the lenght of string
print(len(str))
# Print the string 2 times
print(str * 2)
#print the string slicing means from and upto u want to show the string
print(str[:3])
print(str[1:5])
print(str[-4:-1])
#remove the white space from the beginning of string
print(str.strip())
#Print lower and upper case string
print(str.lower())
print(str.upper())
# To replace the string with existing
print(str.replace("H", "J"))
#To split the string into substrings
print(str.split(","))
# To check whether the string present or not
x = "ell" in str
print(x)
x = "ell" not in str
print(x)
# to concatinate the string
a = "abc"
b = "xyz"
c = a + "" + b
print(c)
# formatting used  in string
print("my name is {}".format(a))