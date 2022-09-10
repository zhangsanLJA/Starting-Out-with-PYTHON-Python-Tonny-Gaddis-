def main():
    zhi_fang=float(input('请输入脂肪克数： '))
    tan_shui_hua_he_wu=float(input('请输入碳水化合物克数： '))
    ka_lu_li=ka(zhi_fang,tan_shui_hua_he_wu)
    print(f'一共有：{ka_lu_li}卡路里热量！')

def ka(num1,num2):
    return num1*9+num2*4

if __name__=='__main__':
    main()
