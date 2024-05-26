def user_info(*args):
    print(args)

#('TOM',)
user_info('TOM')
#('TOM',18)
user_info('TOM',18)


#关键字传递
def user_info(**kwargs):
    print(kwargs)
user_info(name='TOM',age=18,id=110)
#{'name': 'TOM', 'age': 18, 'id': 110}