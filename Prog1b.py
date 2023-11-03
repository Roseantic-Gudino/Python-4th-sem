'''
val=input("Enter a number: ")
if val==val[::-1]:
    print("The number is palindrome")
else:
    print("Not a palindrome")

for i in range(10):
    if val.count(str(i))>0:
        print(str(i),"appears",val.count(str(i)),"times")
'''
'''
class Palindrome:
    def meth1(self,p):
        if p==p[::-1]:
            print("The number is palindrome")
        else:
            print("Not a palindrome")
        for i in range(10):
            if val.count(str(i))>0:
                print(str(i),"appears",val.count(str(i)),"times")   
val=input("Enter a number")
p=Palindrome()
p.meth1(val)

'''
'''
def Palin():
    val=input("Enter a number: ")
    if val==val[::-1]:
        print("The number is palindrome")
    else:
        print("Not a palindrome")

    for i in range(10):
        if val.count(str(i))>0:
            print(str(i),"appears",val.count(str(i)),"times")

p=Palin()
'''
