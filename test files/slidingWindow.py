def window(data,size):
    for i in range(0,len(data),size):
        yield data[i:i+size]
gen=window(list(range(0,11)),3)
for i in gen:
    print(i) 