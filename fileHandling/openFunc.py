'''# #modes=
# #w - write
# #r - read
# #a - append
# #r+ - read and write
# #w+ - write and read
# #a+ - append and read
# #b - binary
# #t - text
# #rt - read text
# #rb - read binary
# #wt - write text
# #wb - write binary
# #at - append text
# #ab - append binary

file=open("sample.txt","w")
file.write("Hello World\n")
file.writelines(["Hello World2\n", "Hello World3\n", "Hello World4\n"])
file.close()

file=open("sample.txt","a")
file.write('This is a new line\n')
file.close()

file=open("sample.txt","r")
print(file.read())
file.close()

with open("sample.txt","r") as file:
    print(file.read())


with open("sample.txt","r") as file:
    for line in file.readlines():
        print(line.strip())

#read has 3 methods:
#read() - reads the entire file -> file.read() -> file.read(5) - reads first 5 characters
#readline() - reads one line at a time -> file.readline() -> file.readline(5) - reads first 5 characters of first line
#readlines() - reads all lines at a time -> file.readlines() -> file.readlines(5) - reads first 5 characters of all lines


with open("sample.txt","w") as file:
    file.write("Hello World\n")
    file.write("Hello World2\n")
    file.write("Hello World3\n")
    file.write("Hello World4\n")

with open("sample.txt","w") as file:
    file.writelines(["Hello World\n", "Hello World2\n", "Hello World3\n", "Hello World4\n"])

#write has 2 methods:
#write() - writes a single string
#writelines() - writes multiple strings'''

with open("sample.txt","r") as file:
    print('there are',len(file.read()),'characters in the file')
    file.seek(0)
    print('there are',len(file.readlines()),'lines in the file')
    file.seek(0)
    print('there are',len(file.read().split()),'words in the file')
