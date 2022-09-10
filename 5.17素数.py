def main():
    num=int(input('请输入一个正整数： '))
    found=is_prime(num)
    if found:
        print(f'{num}是一个素数！')
    else:
        print(f'{num}不是一个素数！')

def is_prime(num1):
    found=True
    for x in range(2,num1):
        if num1%x==0:
            found=False
    if found:
        return True
    else:
        return False

if __name__=='__main__':
    main()
            
