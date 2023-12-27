largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        xx = int(num)
    except:
        print('Invalid input')
        continue
    if largest is None or xx > largest:
       largest = xx
    elif smallest is None or xx < smallest:
       smallest = xx   
    #print(num)
print("Maximum is", largest)
print("Minimum is", smallest)