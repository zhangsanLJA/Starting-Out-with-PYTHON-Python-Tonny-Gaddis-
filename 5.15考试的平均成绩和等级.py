def main():
    num1=inr()
    num2=inr()
    num3=inr()
    num4=inr()
    num5=inr()
    ping_jun_shu=calc_average(num1,num2,num3,num4,num5)
    print(f'平均数是：{ping_jun_shu:.2f}')
    determine_grade(num1)
    determine_grade(num2)
    determine_grade(num3)
    determine_grade(num4)
    determine_grade(num5)

def inr():
    return int(input('请输入一门科目的分数： '))

def calc_average(num1,num2,num3,num4,num5):
    return (num1+num2+num3+num4+num5)/5

def determine_grade(num):
    if num<=100 and num>=90:
        print('等级为A')
    elif num>=80:
        print('等级为B')
    elif num>=70:
        print('等级为C')
    elif num>=60:
        print('等级为D')
    elif num>=0:
        print('等级为F')

if __name__=='__main__':
    main()
