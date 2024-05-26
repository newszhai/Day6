def wd(name,tiwen,type='居家隔离'):
    if(tiwen<=37.5):
        print(f"{name}您的体温小于等于37.5，体温正常")
    else:
        print(f"{name}您的体温大于37.5，需要隔离，隔离方式为{type}")
wd(name='小明',tiwen=38.5)