def main():
    free=float(input('请输入购买金额： '))
    zhou_shui=zhou(free)
    guo_shui=guo(free)
    print(f'州税是{zhou_shui:.2f}')
    print(f'国家税是{guo_shui:.2f}')
    print(f'总消费税是{zhou_shui+guo_shui:.2f}')
    print(f'总消费额是{zhou_shui+guo_shui+free:.2f}')

def zhou(num):
    return num*0.05

def guo(num):
    return num*0.025

if __name__=='__main__':
    main()
