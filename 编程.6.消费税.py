def main():
    sui=float(input('请输入购买金额： '))
    print(f'购买金额是：{sui:^8,.2f}')
    print(f'州消费税是：{sui*0.05:^8,.2f}')
    print(f'国家消费税：{sui*0.025:^8,.2f}')
    print(f'总消费税：{sui*0.075:^8,.2f}')
    print(f'总消费额：{sui*0.075+sui:^8,.2f}')

if __name__=='__main__':
    main()
