def lengthOfLongestSubstring(self, s: str) -> int:
    maxlen = 0
    substrtemp = ""
    for char in s:
        if char in substrtemp:
            maxlen = max(len(substrtemp), maxlen)
            substrtemp = substrtemp.split(char)[1]
            substrtemp += char
        else:
            substrtemp += char    
    maxlen = max(len(substrtemp), maxlen)
    return maxlen
