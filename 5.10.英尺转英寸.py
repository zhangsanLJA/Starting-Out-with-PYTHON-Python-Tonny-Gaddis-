def main():
    inch=float(input('请输入英尺数： '))
    incun=feet_to_inches(inch)
    print(f'转化成为英寸为：{incun:.2f}')

def feet_to_inches(num1):
    return num1*12

if __name__=='__main__':
    main()
