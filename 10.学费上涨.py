FREE=8000
for x in range(5):
    free=FREE*(1+0.03)**x
    print(f'第{x+1}年的学费是： {free:,.2f}')
