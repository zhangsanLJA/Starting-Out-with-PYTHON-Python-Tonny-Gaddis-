time=int(input('请输入你的秒数： '))
if time>=86400:
    day=time//86400
    over1=time%86400
    hour=over1//3600
    over2=over1%3600
    mine=over2//60
    s=over2%60
    print('day:',day,'hour:',hour,'mine:',mine,'second:',s)
elif time>=3600:
    hour=time//3600
    over1=time%3600
    mine=over1//60
    s=over1%60
    print('hour:',hour,'mine:',mine,'second:',s)
elif time>=60:
    mine=time//60
    s=time%60
    print('mine:',mine,'sacond:',s)
elif time>=0:
    print('second:',time)
else:
    print('ERROR')
