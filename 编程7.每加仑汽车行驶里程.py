def main():
    Md=float(input('请输入行驶里程（单位千米）： '))
    Gogu=float(input('请输入消耗汽油的加仑数： '))
    MGP=Md/Gogu
    print(f'汽车的MPG：{MGP:<8,.2f}')

if __name__=='__main__':
    main()
