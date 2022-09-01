num=float(input('请输入一个数求和，负数截至： '))
add=0
while num>=0:
    add+=num
    num=float(input('请输入一个数求和，负数截至： '))
print(f'求和结果是： {add}')
    
