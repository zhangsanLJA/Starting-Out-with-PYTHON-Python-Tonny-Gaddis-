xiao_fei_shui=0.07
xiaofeizonge=float(input('请输入消费总额： '))
xiaofeishui=xiaofeizonge*xiao_fei_shui
print(f'消费税总额为：{xiaofeishui:,.2f}')
print(f'应付款为： {xiaofeishui+xiaofeizonge:,.2f}')
