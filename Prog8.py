class Palindrome_str:
    def __init__(self):
        self.isPalindrome = False

    def checkPalindrome(self,St):
        if St == St[::-1]:
            self.isPalindrome = True
        else:
            self.isPalindrome = False

        return self.isPalindrome

class Palindrome_Int:
    def __init__(self):
        self.isPalindrome = False

    def checkPalindrome(self,val):
        temp = val
        reverse = 0
        while temp != 0:
            remainder = temp % 10
            reverse = (reverse*10) + remainder
            temp = temp // 10

        if val == reverse:
            self.isPalindrome = True
        else:
            self.isPalindrome = False

        return self.isPalindrome

st = input("Enter a string: ")

stObj = Palindrome_str()

if stObj.checkPalindrome(st):
    print("String is a palindrome")
else:
    print("String is not a palindrome")

val = int(input("Enter an integer: "))

intObj = Palindrome_Int()

if intObj.checkPalindrome(val):
    print("Integer is a palindrome")
else:
    print("Integer is not a palindrome")
