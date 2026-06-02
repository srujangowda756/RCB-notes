import os

#os.makedirs("test_folder")
#os.rmdir("test_folder")

#print(os.path.isfile('test_folder'))
f= open('test.txt', 'a')
f.write('\nHello World')
f.writelines(['\nHello World 3', '\nHello World 4'])
f.close()


d=open('test.txt', 'r')
print(d.read())
print(d.tell())
d.seek(3,0)
print(d.tell())

os.rmdir("test_folder")
