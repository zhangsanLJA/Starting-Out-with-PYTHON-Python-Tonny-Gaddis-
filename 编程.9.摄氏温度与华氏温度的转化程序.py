def main():
    sheshidu=float(input('请输入当前温度（单位:摄氏度）： '))
    print(f'{sheshidu:^8.2f}摄氏度转化后为：{sheshidu*9/5+32:^8.2f}华氏度。')

if __name__=='__main__':
    main()
