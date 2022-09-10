def main():
    liang_shu=0
    file_name=open(r'D:\number.txt','r')
    number=file_name.readline()
    while number!='':
        liang_shu+=1
        number=number.rstrip()
        print(number)
        number=file_name.readline()
    print(liang_shu)

if __name__=='__main__':
    main()
