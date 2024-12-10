principle = 0
rate = 0
time = 0

while True:
    principle = float(input('Enter the principle amount: '))
    if principle < 0:
        print('Principle can not be less than or equal to zero')
    else:
        break
        
while True:
    rate = int(input('Enter the rate Interest: '))
    if rate < 0:
        print('rate can not be less than or equal to zero')
    else:
        break

while True:
    time = float(input('Enter the time period in years: '))
    if time < 0:
        print('Time can not be less than or equal to zero')
    else:
        break
        

total = principle * pow((1 + rate / 100), time)
print(f'Balance after {time} year/s: {total:.2f}INR')