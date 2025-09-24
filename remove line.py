file1 = ('Codingal.txt', 'r')
file2 = ('Codingal updateed.txt', 'w')
for line in file1.readlines():
    if not (line.startswith('coding')):
        print(line)
        file2.write(line)
file2.close()
file1.close()