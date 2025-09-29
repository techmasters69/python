new_file = open('New_file.txt', 'x')
new_file.close()
import os
print("checking if my_file exists or not....")
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
else:
    print("the file dose not exist")
my_file = open("my_file.txt", "w")
my_file.write("hi i am penguin and i am 1 yr old.")
my_file.close()
