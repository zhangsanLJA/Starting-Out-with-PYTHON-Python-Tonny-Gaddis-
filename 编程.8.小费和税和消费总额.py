def main():
    feiyong=float(input('请输入消费总额(单位$)： '))
    print(f'小费是：{feiyong*0.18:^8,.2f}$')
    print(f'税是：{feiyong*0.07:^8,.2f}$')
if __name__=='__main__':
    main()
