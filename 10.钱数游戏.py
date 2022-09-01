penny=int(input('请输入1分硬币数量： '))
nickel=int(input('请输入5分硬币的数量： '))
dinne=int(input('请输入1角钱硬币数量： '))
quarter=int(input('请输入25分硬币数量： '))
add=penny+5*nickel+10*dinne+25*quarter
if add==100:
    print('win')
else :
    print('fail')
