def main():
    p=float(input('最初存入账户的本金金额： '))
    r=float(input('对应存款账户的年利率: '))
    n=float(input('每年计算复利的次数: '))
    t=float(input('获取存款的年数: '))
    a=p*(1+r/100*n)**(n*t)
    print(f'指定年份的总金额是： {a:^8,.2f}$')

if __name__=='__main__':
    main()
    
