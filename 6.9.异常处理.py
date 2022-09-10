def main():
    add=0
    num=0
    try:
        file=open(r'D:\number.txt','r')
        number=file.readline()
        while number!='':
            number=int(number.rstrip())
            add+=number
            num+=1
            number=file.readline()
        file.close()
        print(f'平均值为： {add/num:.2f}')

    except IOError as stt:
        print(stt)

    except ValueError as srr:
        print(srr)

if __name__=='__main__':
    main()
