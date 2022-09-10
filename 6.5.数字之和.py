def main():
    file=open(r'D:\number.txt','r')
    add=0
    number=file.readline()
    while number!='':
        number=float(number.rstrip())
        add+=number
        number=file.readline()
    print(add)

if __name__=='__main__':
    main()
