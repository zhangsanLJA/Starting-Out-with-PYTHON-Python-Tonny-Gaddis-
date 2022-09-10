def main():
    file=open(r'D:\number.txt','r')
    add=0
    num=0
    number=file.readline()
    while number!='':
        number=float(number.rstrip())
        num+=1
        add+=number
        number=file.readline()
    print(add/num)

if __name__=='__main__':
    main()
