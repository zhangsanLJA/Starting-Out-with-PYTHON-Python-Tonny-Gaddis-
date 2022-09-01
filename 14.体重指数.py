weight=float(input('请输入体重（单位;磅）： '))
hight=float(input('请输入身高（单位：英寸）： '))
BMI=weight*703/hight**2
if BMI>=18.5 and BMI<=25:
    print('身体是最佳的！')
elif BMI>0 and BMI<18.5:
    print('身体偏瘦')
elif BMI>25:
    print('体重超重')
else:
    print('ERROR')
