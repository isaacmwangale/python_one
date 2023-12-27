zork=0
total=0
print('before', zork)
for num in [3,41,12,9,74,15]:
    zork = zork + 1
    total = total + num
    mean = total/zork
    print(zork, num, total)
print('after', zork,total,mean)