def main():
    file_number=input('请输入文件名： ')
    file=open(file_number,'r')
    for x in range(5):
        read_number=file.readline()
        read_number=read_number.rstrip()
        print(x+1,'行',read_number)
    file.close()

if __name__=='__main__':
    main()
