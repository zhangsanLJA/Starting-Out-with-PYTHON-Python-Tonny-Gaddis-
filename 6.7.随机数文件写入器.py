import random

def main():
    file=open(r'D:\number.txt','w')
    ci_shu=int(input('请输入一个循环次数： '))
    for x in range(ci_shu):
        number=random.randint(1,500)
        file.write(f'{number}\n')
    file.close()

if __name__=='__main__':
    main()
