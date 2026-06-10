"""
1、选择语句
    * if-else 语句
    * match-case 语句：case 后面不能写 break、会自动结束当前 case；多个条件对应同一个执行体时，用 | 合并条件；_ 相当于 default
    match-case 语句一般用在枚举的判断上，其它的一般就用 if-else 语句
"""
age = 18
if age >= 18:
    print("成年")
else:
    print("未成年")

status = 1
match status:
    case 1:
        print("正常用户")
    case 2 | 3:
        print("封禁用户")
    case _:
        print("未知状态")

"""
2、循环语句
    * for 语句
    * while 语句
    for 语句更适遍历容器或者跟次数相关的循环，while 语句更适合跟某个条件相关的循环
"""
# for 语句遍历容器
for name in ["张三", "李四", "王五"]:
    print(name)

# for 语句跟次数相关的循环，一般会配合 range() 使用
# range(stop): 返回 [0, stop) 的整数序列
# range(start, stop): 返回 [start stop) 的整数序列
# range(start, stop, step): 返回 [start stop) 的整数序列、步长为 step
for i in range(3):
    print(i)

# while 语句跟某个条件相关的循环
i = 100
while i >= 98:
    print(i)
    i -= 1

"""
3、转向语句
    * break 语句
    Python 里 catch-case 语句不需要写 break，所以 break 语句只能用在 for语句、while 语句中
    break 语句的作用是用来终止其所在的那一层 for语句、while 语句，再外一层的语句它就管不了了，更外一层的函数它就更管不了了

    * continue 语句
    continue 语句只能用在 for语句、while 语句中
    continue 语句的作用是用来终止其所在的那一层 for语句、while 语句的某一次循环并立即继续下一次循环，再外一层的语句它就管不了了，更外一层的函数它就更管不了了
    
    * return 语句
    return 语句可以用在很多地方
    return 语句的作用是用来退出其所在的函数
"""