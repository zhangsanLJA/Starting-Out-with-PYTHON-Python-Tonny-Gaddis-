yusuan=float(input('预算多少：'))
add=0
num1=float(input('请输入开销： '))
str1=input('是否还有输入开销（yes or no）： ')
while str1=='yes':
    add+=num1
    num1=float(input('请输入下一笔开销: '))
    str1=input('是否还有输入开销（yes or no）:')
if add<=yusuan:
    print('低于预算')
else:
    print('超出预算')
