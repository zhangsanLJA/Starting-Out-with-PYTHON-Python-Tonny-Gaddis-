weight=float(input('请输入行李重量： '))
if weight>=0 and weight<=2:
    FEW=1.5
    feiyong=weight*FEW
    print(feiyong)
elif weight>2 and weight<=6:
    FEW=3
    feiyong=weight*FEW
    print(feiyong)
elif weight>6 and weight<=10:
    FEW=4
    feiyong=weight*FEW
    print(feiyong)
elif weight>10:
    FEW=4.75
    feiyong=weight*FEW
    print(feiyong)
else:
    print('ERROR')
