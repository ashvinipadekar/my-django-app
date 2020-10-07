t1=("ashviini","datta","padekar")
# to print tuple and find out the lenght
print(t1)
print(len(t1))
# add the two tuple in third tuple
t2=("riehansh",)
t3=t1+t2
print(t3)
#shows the value of the tuple
count=0
for i in t1:
    print("t1[{}]={}".format(count,i))
    count=count+1
# to print slicing of tuple
print(t1[:2])
print(t1[-1])
print(t2*4)
# To check whether the item present in tuple or not
print("ashviini" in t1)
