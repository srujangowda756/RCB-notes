# isPangram
st='The quick brown fox jumps over the lazy dog'
def isPangram(elem):
    if len(elem)<26:
        return False
    elem = elem.lower()
    for i in range(26):
        if chr(97+i) not in elem:
            return False
    return True
print(isPangram(st))

def isPangram1(elem):
    elem = elem.lower()
    res=''
    for ch in elem:
        if ch.isalpha():
            res += ch
    return len(set(res)) == 26

def isPangram2(elem):
    res={ch.lower() for ch in elem if ch.isalpha()}
    return len(res) == 26
print(isPangram1(st))
print(isPangram2(st))



#anagram 


t=(1,2)*3
print(t)
print(t[1])

print(2**3**2)

