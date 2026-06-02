from copy import deepcopy
l2=[10,20,[30,40]]
l3=deepcopy(l2)
print(l3)
l2[2][0]=50
print(l3)
print(l2)
