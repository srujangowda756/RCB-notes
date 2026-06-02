def dec_to_hex(num):
    hex = 16
    result = ""
    while num > 0:
        remainder = num % hex
        if remainder < 10:
            result = str(remainder) + result
        else:
            result = chr(65 + remainder - 10) + result
        num = num // hex
    return result

n = int(input("Enter a decimal number: "))
print(dec_to_hex(n))