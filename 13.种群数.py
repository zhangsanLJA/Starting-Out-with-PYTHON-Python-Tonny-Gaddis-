snum=float(input('种群的初始数目： '))
speed=float(input('平均每天的增长数目： '))
noday=int(input('允许繁殖的天数： '))
print('Day Approximate\tPopulation')
for x in range(noday):
    num=snum*(1+speed)**x
    print(f'{noday+1}\t{num}')
    
