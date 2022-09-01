a1=float(input('请输入长方形的长： '))
b1=float(input('请输入长方形的宽： '))
a2=float(input('请输入长方形的长： '))
b2=float(input('请输入长方形的宽： '))
if a1*b1>a2*b2:
    print(f'第一个长方形的面积最大，面积是{a1*b1:,.2f}')
elif a1*b1==a2*b2:
    print(f'两个长方形面积相等，面积都是{a1*b1:,.2f}')
else:
    print(f'第二个长方形的面积最大，面积是{a2*b2:,.2f}')
