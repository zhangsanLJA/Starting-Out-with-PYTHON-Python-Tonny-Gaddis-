def main():
    add=0
    num=0
    file=open(r'D:\number.txt','r')
    for number in file:
        number=float(number.rstrip())
        num+=1
        add+=number
    file.close()
    print(f'数据的总和是： {add}\n一共有 {num}个随机数')

if __name__=='__main__':
    main()
