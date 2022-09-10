def  main():
    worth=float(input('请输入这给物品的更换成本： '))
    bao_xian_free=sciens(worth)
    print(f'购买财产保险的最低金额是：{bao_xian_free:.2f}')

def sciens(num):
    return num*0.8

if __name__=='__main__':
    main()
