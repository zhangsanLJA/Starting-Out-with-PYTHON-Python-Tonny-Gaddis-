#Serendipity Booksellers
#book club
book=int(input('请输入你买书的数目： '))
if book>=0 and book<2:
    point=0
elif book>=2 and book<4:
    point=5
elif book>=4 and book<6:
    point=15
elif book>=6 and book<8:
    point=30
elif book>=8:
    point=60
else :
    print('ERROR')
print('点数是',point)
