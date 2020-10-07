"""
l1=["banana","apple","cherry"]
# To find the lenght of list
print(len(l1))
# to change the value of current element
l1[1]="strawberry"
print(l1)
# To check  whether the element present in list
if "apple" in l1:
    print("yes")
#Add item or isert item in list
l1.append(,",o,range")
print(l1)
l1.insert(2,"guava")
print(l1)
# remove , pop clear the list item or list
l1.remove("guava")
print(l1)
#conactinating two list
l2=[1,2,3]
l3=l2+l1
print(l3)
# copy() the list
list1=["ash","datta"]
list2=list1.copy()
print(list2)
# to find max and min in list
ll1=[10,20,30,40]
print(max(ll1))
print(min(ll1))


#***** To print empty l,ist stored with unique value
l1=[1,2,2,3,55,98,65,65,13,29]
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)

# To print sum of elements in the list
l1=[1,2,3,4,5]
sum=0
for i in l1:
    sum=sum+i
print(sum)

"""
# ### WAP to find list consist of atleast one common elelment
l1 = [10, 20, 30, 40]
l2 = [40, 56, 98, 89, 70]
for i in l1:
    for j in l2:
        if i==j:
            print(i)
