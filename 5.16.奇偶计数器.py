import random
def main():
    add=0
    app=0
    for x in range(100):
        num=random.randint(1,100)
        if num%2==0:
            add+=1
        else:
            app+=1
    print(f'一共有{add}个偶数，{app}个奇数')

if __name__=='__main__':
    main()
