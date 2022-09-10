def main():
    file=open(r'D:\golf.txt','w')
    again='y'
    while again=='y':
        name=input('请输入球员名字： ')
        file.write(name+'\n')
        cheng_ji=input('请输入成绩： ')
        file.write(cheng_ji+'\n')
        again=input('是否愿意继续输入y,or Y: ')

    file.close()

if __name__=='__main__':
    main()
