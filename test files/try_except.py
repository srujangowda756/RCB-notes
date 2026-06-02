
try:
    a=5
    b=0
    print(a/b)
except Exception as e:
    print('Cannot divide by zero')
    print(e)
else:
    print('Division successful')
finally:
    print('Execution completed')


print('=================================================')

try:
    print('abc'+123)
except Exception as e:
    print(e)

print('=================================================')

try:
    import a
except Exception as e:
    print(e)

print('=================================================')

try:
    print(i)
except Exception as e:
    print(e)

print('=================================================')

