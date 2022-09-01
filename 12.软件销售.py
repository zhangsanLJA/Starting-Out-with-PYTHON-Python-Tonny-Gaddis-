buy_num=int(input('请输入购买软件数量： '))
if buy_num>=0 and buy_num<=19:
    zheko=0.1
elif buy_num>=20 and buy_num<=49:
    zheko=0.2
elif buy_num>=50 and buy_num<=99:
    zheko=0.3
elif buy_num>=100:
    zheko=0.4
else:
    print('ERROR')
huafei=buy_num*(1-zheko)*99
print(f'折扣的价格{zheko*99*buy_num}')
print('总款项：',huafei)
