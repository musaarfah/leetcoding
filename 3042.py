def isPrefixandSuffix(str1,str2):
    slice=len(str1)

    prefix=str2[:slice]
    suffix=str2[-slice:]

    if str1==prefix and str1==suffix:
        return True
    else:
        return False
    
def countPrefixSuffixPairs(words):
    count=0
    for i in range(len(words)):
        for j in range(i+1,len(words)):
            if isPrefixandSuffix(words[i],words[j]):
                count+=1

    return count

words = ["pa","papa","ma","mama"]
print(countPrefixSuffixPairs(words))



