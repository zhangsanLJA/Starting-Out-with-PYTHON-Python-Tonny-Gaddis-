import random
a=random.randint(0,1000)
b=random.randint(0,1000)
print(    a)
print(    b)
sud=int(input(f'请输入{a}和{b}的和： '))
if sud==a+b:
    print('祝贺回答正确')
else:
    print(f'答案不正常\n正确答案是 {a+b}')
