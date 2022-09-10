import random

def main():
    computer_num=random.randint(1,3)
    user=input('请输入用户的选择： ')
    if computer_num==1:
        print('计算机选择了  石头')
    elif computer_num==2:
        print('计算机选择了  布')
    else:
        print('计算机选择了  剪刀')
    if user=='石头':
        num=1
    elif user=='布':
        num=2
    elif user=='剪刀':
        num=3
    else:
        print("ERROR")
    if computer_num==1 and num==3:
        print('计算机胜')
    elif computer_num==1 and num==2:
        print('用户胜')
    elif computer_num==2 and num==1:
        print('计算机胜')
    elif computer_num==2 and num==3:
        print('用户胜')
    elif computer_num==3 and num==1:
        print('用户胜')
    elif computer_num==3 and num==2:
        print('计算机赢')
    else:
        print('平局')

if __name__=='__main__':
    main()
