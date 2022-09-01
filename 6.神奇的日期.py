year=int(input('请输入两位数年份： '))
mouth=int(input('请输入月份： '))
day=int(input('请输入日期： '))
if year==mouth*day:
    print('这个日期真是一个神奇的日期！')
else:
    print('这个日期不神奇！')
