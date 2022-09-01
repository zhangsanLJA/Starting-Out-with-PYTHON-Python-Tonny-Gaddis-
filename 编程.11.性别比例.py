def main():
    man=int(input('请输入一个班级的男生数目： '))
    woman=int(input('请输入一个班级的女生数目： '))
    print(f'男生的性别比例是：{man/(man+woman):^8.2%}')
    print(f'女生的性别比例是: {woman/(man+woman):^8.2%}')

if __name__=='__main__':
    main()
