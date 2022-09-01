day=int(input('工作天数： '))
add=0
for x in range(day):
    daymoney=2**x
    add+=daymoney
print(f'筹薪数：{add}')
