year=int(input('请输入年数： '))
add=0
for x in range(1,year+1):
    addd=0
    for y in range(1,13):
        wheather=float(input(f'请输入{x}年{y}月的降雨量： '))
        addd+=wheather
    print(f'这一年每月的降雨量:{addd/12}')
    add+=addd
print(f'这短时间平均每月降雨量为{add/(year*12)}')
