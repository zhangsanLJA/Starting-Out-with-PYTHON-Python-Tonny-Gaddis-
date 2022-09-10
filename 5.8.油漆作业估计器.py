def main():
    mian_ji=float(input('请输入所刷面积大小： '))
    you_jia=float(input('请输入油漆每加仑价格： '))
    print(f'所需油漆加仑数： {mian_ji/112:.2f}')
    print(f'所需人工劳动时间： {mian_ji/112*8:.2f}')
    you_fei=you(mian_ji,you_jia)
    ren_gong_fei=ren(mian_ji)
    print(f'油漆所需费用为： {you_fei:.2f}')
    print(f'人工费为： {ren_gong_fei:.2f}')
    print(f'油漆作业的总成本是： {you_fei+ren_gong_fei:.2f}')

def you(num1,num2):
    return num1/112*num2

def ren(num1):
    return num1/112*8*35

if __name__=='__main__':
    main()
