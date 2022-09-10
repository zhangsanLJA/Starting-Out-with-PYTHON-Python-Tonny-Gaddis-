def main():
    jia_zhi=float(input('请输入这个物品的价值： '))
    gu_jia=gu(jia_zhi)
    cai_chan_shui=shui(gu_jia)
    print(f'估价为： {gu_jia:.2f}\n财产税为： {cai_chan_shui:.2f}')

def gu(num):
    return num*0.6

def shui(num):
    return num/100*0.72

if __name__=='__main__':
    main()
