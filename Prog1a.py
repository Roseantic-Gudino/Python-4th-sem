'''
m1=int(input("Enter marks for test1: "))
m2=int(input("Enter marks for test2: "))
m3=int(input("Enter marks for test3: "))

if m1<=m2 and m1<=m3:
    avg=(m3+m2)/2
elif m2<=m1 and m2<=m3:
    avg=(m1+m3)/2
elif m3<=m2 and m3<=m2:
    avg=(m1+m2)/2

print("Average of best of two test marks= ",avg)

'''
'''
def pro():
    m1=int(input("Enter marks for test1: "))
    m2=int(input("Enter marks for test2: "))
    m3=int(input("Enter marks for test3: "))

    if m1<=m2 and m1<=m3:
        avg=(m1+m2)/2
    elif m2<=m1 and m2<=m3:
        avg=(m1+m3)/2
    elif m3<=m2 and m3<=m2:
        avg=(m1+m2)/2
    print("Average of best of two test marks= ",avg)
avg=pro()
'''
'''
class Avg:
    def pro(self):
        m1=int(input("Enter marks for test1: "))
        m2=int(input("Enter marks for test2: "))
        m3=int(input("Enter marks for test3: "))

        if m1<=m2 and m1<=m3:
            avg=(m1+m2)/2
        elif m2<=m1 and m2<=m3:
            avg=(m1+m3)/2
        elif m3<=m2 and m3<=m2:
            avg=(m1+m2)/2
        print("Average of best of two test marks= ",avg)

a=Avg()
a.pro()
'''

n1=0
n2=1
n3=n1+n2
for i in range (0,10):
    n3=n1+n2
    n3,n2=n2,n1
    print(n3)


