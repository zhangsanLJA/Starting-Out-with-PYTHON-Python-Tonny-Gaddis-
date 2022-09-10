def main():
    xiao_shou_e=float(input('亲输入本月营业额： '))
    zhou_shui,qu_shui=shui(xiao_shou_e)
    print(f'区县税总额： {qu_shui:.2f}')
    print(f'州税总额： {zhou_shui:.2f}')
    print(f'总销售税额： {qu_shui+zhou_shui:.2f}')

def shui(num1):
    return num1*0.05,num1*0.025

if __name__=='__main__':
    main()
