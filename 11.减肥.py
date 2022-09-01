weight=float(input('请输入你的体重： '))
print('如果按照这个节食方案')
for x in range(1,7):
    lose_weight=x*500
    print(f'第{x}个月\t减重{lose_weight}')
