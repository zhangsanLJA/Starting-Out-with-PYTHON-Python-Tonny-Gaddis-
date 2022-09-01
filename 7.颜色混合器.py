color1=input('请输入三种三原色（红色、蓝色，黄色） 颜色1： ')
color2=input('亲输入三种三原色（红色、蓝色、黄色） 颜色2： ')
if (color1!='red' or color1!='blue' or color1!='yellow')and(color2!='red' or color2!='blue' or color2!='yellow'):
    if (color1=='red' and color2=='blue') or (color1=='blue' and color2=='red'):
        print('purple')
    if (color1=='red' and color2=='yellow') or (color1=='yellow' and color2=='red'):
        print('orange')
    if (color1=='blue' and color2=='yellow') or (color1=='yellow' and color2=='blue'):
        print('green')
else:
    print('ERROR')
