s=input("Enter a sentence:")
w,d,u,l=0,0,0,0
words=s.split()
w=len(words)
for c in s:
    if c.isdigit():
        d+=1
    elif c.isupper():
        u+=1
    elif c.islower():
        l+=1

print("The number of words: ",w)
print("The number of digits: ",d)
print("The number of uppercase letters: ",u)
print("The number of lowercase letters: ",l)
