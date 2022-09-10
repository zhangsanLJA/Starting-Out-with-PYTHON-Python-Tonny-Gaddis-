def main():
    p=float(input('请输入账户现值： '))
    i=float(input('请输入月利率： '))
    t=int(input('请输入月利率： '))
    f=get_money(p,i,t)
    print(f'未来价值是: {f}')

def get_money(num1,num2,num3):
    return num1*(1+num2)**num3

if __name__=='__main__':
    main()
