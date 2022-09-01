year=int(input('请输入年份： '))
if year%100==0 and year%400==0:
    sign=True
elif year%100!=0 and year%4==0:
    sign=True
else:
    sign=False
if sign:
    print('二月份有29天')
else:
    print('二月份有28天')
