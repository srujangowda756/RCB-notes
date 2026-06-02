print('\n'.join(' '.join(str(j) for j in range(1, i+1)) for i in range(1,6)))

print('=========================================')

k=1
for i in range(5):
    for j in range(i):
        print(k,end=' ')
        k+=1
    print()