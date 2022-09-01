speed=float(input('What is the speed of the vehicle in mph? '))
hour=float(input('How many hours has it traveled? '))
print('hour\tDistannce Traveled')
for x in range(int(hour)):
    print(f'{x+1}\t{(x+1)*speed}')
