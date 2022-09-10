def main():
    file=open(r'D:\golf.txt','r')
    name=file.readline()
    while name!='':
        num=file.readline()
        name=name.rstrip()
        num=num.rstrip()
        print(name)
        print(num)
        name=file.readline()
    file.close()

if __name__=='__main__':
    main()
        
