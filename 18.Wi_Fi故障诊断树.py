str1=input('问题修复了吗？ ： ')
if str1=='no':
    str2=input('请重新启动路由器并请求链接： ')
    if str2=='yes':
        str3=input('问题修复好了吗： ')
        if str3=='no':
            str4=input('确保链接路由器和调解抑制器的线缆插头已稳固的插在插槽里面： ')
            if str4=='no':
                str5=input('问题修复了吗： ')
                if str5=='no':
                    str6=input('移动路由器到一个新的位置并请求链接： ')
                    if str6=='no':
                        str7=input('问题修复了吗： ')
                        if str7=='no':
                            print('换一个新路由器')
