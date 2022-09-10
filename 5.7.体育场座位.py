def main():
    a=int(input('请输入a座位数： '))
    b=int(input('请输入b座位数： '))
    c=int(input('请输入c座位数： '))
    shou_ru=shouyi(a,b,c)
    print(f'图书馆收益是： {shou_ru:.2f}')

def shouyi(num1,num2,num3):
    return num1*20+num2*15+num3*10

if __name__=='__main__':
    main()
