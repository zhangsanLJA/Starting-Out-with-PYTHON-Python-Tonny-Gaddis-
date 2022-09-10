G=9.8
def main():
    for x in range(1,11):
        d=falling_distance(x)
        print(f'{x}秒下降的距离是：{d:.2f}')

def falling_distance(num1):
    return 1/2*G*num1**2

if __name__=='__main__':
    main()
