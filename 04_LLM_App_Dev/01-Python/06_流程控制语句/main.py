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