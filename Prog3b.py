import difflib

def string_similarity(str1,str2):
    result=difflib.SequenceMatcher(a=str1.lower(),b=str2.lower())
    return result.ratio()

str1=input("Enter String1:")
str2=input("Enter String2:")
print("Similarity between two said strings: ")
print(string_similarity(str1,str2))
