def main():
    for x in range(1,100):
        found=is_prime(x)
        if found:
            print(x,'是素数')

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
