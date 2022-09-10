def main():
    zhi_liang=float(input('请输入这个物体的质量（单位：kg）: '))
    su_du=float(input('请输入这个物体的速度（单位：m/s）: '))
    ke=kinetic_energry(zhi_liang,su_du)
    print(f'该物体的动能KE= {ke:.2f}')

def kinetic_energry(num1,num2):
    ke=1/2*num1*num2**2
    return ke

if __name__=='__main__':
    main()
