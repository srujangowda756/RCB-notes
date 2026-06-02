def hex_to_decimal(num):
    num = num.upper()
    hex=16
    tot=0
    n=len(num)
    d={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
    for i in range(n-1, -1, -1):
        if num[i].isalpha():
            if num[i] in d:
                temp = d[num[i]]
            else:
                return "Invalid hexadecimal number"
        else:
            temp = int(num[i])
        ans=temp*(hex**(n-1-i))
        tot+=ans
    return tot
        
hex_num = input("Enter a hexadecimal number: ")
print(hex_to_decimal(hex_num))