def roman2Dec(numeral):
    d={"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}

    ans=0
    n=len(numeral)
    for(index,character) in enumerate(numeral):
        if index<n-1 and d[character]<d[numeral[index+1]]:
            ans-=d[character]
        else:
            ans+=d[character]
    return ans

romanStr=input("Enter a roman number: ")
print(roman2Dec(romanStr))
