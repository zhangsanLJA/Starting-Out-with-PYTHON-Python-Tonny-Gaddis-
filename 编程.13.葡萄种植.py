def main():
    r=float(input('请输入你的土地每行长度（单位：英寸）： '))
    e=float(input('请输入你的土地端柱组间所占宽度：（单位：英寸）： '))
    s=float(input('亲输入你的葡桃颗与颗之间距（单位：英寸，且不得为0）： '))
    v=(r-2*e)/s
    print(f'每行最佳种植颗数：{v:^8.2f}')

if __name__=='__main__':
    main()
    
