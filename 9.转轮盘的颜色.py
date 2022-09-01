num=int(input('请输入口袋编号： '))
if num==0:
    print('green')
elif num>0 and num<=10:
    if num//2==1:
        print('red')
    else:
        print('black')
elif num>10 and num<=18:
    if num//2==1:
        print('black')
    else:
        print('red')
elif num>18 and num<=28:
    if num//2==1:
        print('red')
    else:
        print('black')
elif num>28 and num<=36:
    if num//2==1:
        print('black')
    else:
        print('red')
else:
    print('ERROR')
