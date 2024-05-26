def fun_default_parameters(param1,param2=2):
    print(param1+param2)
fun_default_parameters(1)
fun_default_parameters(1,5)
# 关键字参数正常调用
def fun_keyword_parameters(param1,param2=2):
    print(param1-param2)
fun_keyword_parameters(param1=5,param2=2)
#关键字参数不按顺序传递
def fun_keyword_parameters(param1,param2=2):
    print(param1-param2)
fun_keyword_parameters(param2=2,param1=5)
#关键字参数和位置参数的混合使用
#位置参数在前，关键字参数在后面
print(fun_keyword_parameters(5,param2=2))
#位置参数在前，关键字参数在后
fun_keyword_parameters(5,param2=2)
#关键字参数在前，位置参数在后
fun_keyword_parameters(param1=1,param2=2)