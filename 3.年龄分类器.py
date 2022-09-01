year_old=float(input('请输入年龄来判断： '))
if year_old>0 and year_old<=1:
    print('这是婴儿')
elif year_old<13:
    print('这是儿童')
elif year_old<20:
    print('这是青年')
else:
    print('成年人')
