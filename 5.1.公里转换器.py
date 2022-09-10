def main():
    num=float(input('请输入公里数： '))
    mile=zhuan(num)
    print(f'{num}公里等于{mile}')

def zhuan(ass):
    return ass*0.6214

if __name__=='__main__':
    main()
