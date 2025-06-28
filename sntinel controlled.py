count = 0
total = 0
x = 0
while x != -1:
    x = float(input('enter a grade, enter -1 to stop entering grades :'))
    total += x
    count += 1

if count > 0:
    avg = total/count
    print(f'The average is{avg}')
else  :
    print('No grades were input')      