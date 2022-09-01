mass=float(input('请输入一个物体的重量（单位：千克）： '))
weight=mass*9.8
if weight<100:
    print('太轻了')
elif weight>500:
    print('太重了')
else:
    print('')
