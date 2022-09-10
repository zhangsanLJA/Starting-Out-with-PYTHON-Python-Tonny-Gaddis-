import random

def main():
    num=random.randint(1,100)
    num1=int(input('请猜一猜一个1到100的整数是多少：'))
    ci_shu=1
    while num!=num1:
        if num<num1:
            print('猜大了')
            ci_shu+=1
        else:
            print('猜小了')
            ci_shu+=1
        print(f'这是第{ci_shu}')
        num1=int(input('请猜一猜一个1到100的整数是多少：'))
    print(f'猜对了这是第{ci_shu}次')

if __name__=='__main__':
    main()

