#open and read its content
file = open('python/Codingal.txt', 'r')
print(file.read())
file.close()
#open file and read its begining 8 characters
file = open('Condingal.txt', 'r')
print("\n read in parts \n")
print(file.read())
file.close()
#append your name and age in the file
file = open('python/Codingal.txt', 'a')
file.write("hi am penguin and i am 1 yr old")
file.close()
