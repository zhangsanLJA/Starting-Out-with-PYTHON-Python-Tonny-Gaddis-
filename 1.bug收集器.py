add=0
for x in range(5):
    print(f'第{x+1}天')
    ldong=int(input('请输入收集到的bug数目： '))
    add+=ldong
print(f'这5天的bug总数是：{add}个')
