'''import re
matchStr=re.finditer("ab", "aabbababababababababbababababba")
count=0
for match in matchStr:
    print(match.start(), match.end(), match.group())
    count+=1
print(count)'''

import re


print("=====================")
count=0
s='Everything is Not Ordinary'
matchStr=re.finditer("a?",s)
for match in matchStr:
    count+=1
print(count)

print("=============")

num='517774763929'
res=re.sub("[0-9]{8}","XXXXXXXX",num)
print(res)

d={'a':20,'b':30,'d':10,'c':10}
sorted_d=dict(sorted(d.items(),key=lambda x:(-x[1],x[0])))
print(sorted_d)