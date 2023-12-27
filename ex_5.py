count = 0
tot = 0.0
while True:
    num = input('Enter any number')
    if num == 'done':
        break
    try:
        h = float(num)
    except:
        print('invalide number')
        continue
        #print(h)
    count = count + 1
    tot = tot + h
print(count,tot,tot/count)