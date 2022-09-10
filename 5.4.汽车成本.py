def main():
    dai_kuan=float(input('请输入这辆车的贷款成本： '))
    bao_xian=float(input('请输入这辆车的保险成本： '))
    qi=float(input('请输入这辆车的气成本： '))
    you=float(input('请输入这辆车的油的成本: '))
    lun_tai=float(input('请输入这辆车的轮胎成本： '))
    wei_xiu=float(input('请输入这辆车的维修费用： '))
    yue_cheng_ben=yue(dai_kuan,bao_xian,qi,you,lun_tai,wei_xiu)
    nian_cheng_ben=nian(dai_kuan,bao_xian,qi,you,lun_tai,wei_xiu)
    print(f'月度成本是{yue_cheng_ben}')
    print(f'年度成本是{nian_cheng_ben}')

def yue(num1,num2,num3,num4,num5,num6):
    return num1+num2+num3+num4+num5+num6

def nian(num1,num2,num3,num4,num5,num6):
    return (num1+num2+num3+num4+num5+num6)*12

if __name__=='__main__':
    main()
