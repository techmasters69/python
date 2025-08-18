num = 29
flag = False
if num > 1:
    #cheak for factors
    for i in range(2, num):
        if(num %i) == 0:
            flag = True
            break
if flag:
    print(num, "is not a prime")
else:
    print(num, "is a prime number")