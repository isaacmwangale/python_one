smallest = None
print('before')
for value in [9,41,3,12,74,15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest,value)
print('after', smallest)