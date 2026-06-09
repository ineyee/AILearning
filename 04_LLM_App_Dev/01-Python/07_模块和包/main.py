"""=========== 使用成员时需要写前缀的导入方式，因为是以模块为单位导入 ==========="""

# 方式一：导入模块时用完整路径，使用成员时也得用完整路径做前缀
#
# 完整路径写起来太长了，不推荐
# import service.user_service
#
# print(service.user_service.user_name)
# print(service.user_service.get_info())

"""
方式二：导入模块时用完整路径 + as 给模块取个短别名，使用成员时就可以用模块的短别名做前缀

推荐，这里体现了 as 的第一个用途：给模块取别名来缩短使用时的模块前缀
"""
# import service.user_service as user
#
# print(user.user_name)
# print(user.get_info())

"""
方式三：导入模块时用 from import，使用成员时就可以只用模块名做前缀

推荐，只需要用模块名做前缀、已经短很多了
"""
from service import user_service

print(user_service.user_name)
print(user_service.get_info())

"""
方式四：导入模块时用 from import + as 给模块取个短别名，使用成员时就可以用模块的短别名做前缀

推荐，如果还是觉得模块名比较长、那就用 as 再缩短点
"""
# from service import user_service as user
#
# print(user.user_name)
# print(user.get_info())

# 方式五：一次性从某个包里导入所有公开模块（__init__.py 里“导出”的模块才是公开模块），这种情况下就必须得用 from import、不能用 import
#
# 不推荐，阅读代码时不能一眼看出 user_service、order_service 来自哪个包
# from service import *
#
# print(user_service.user_name)
# print(user_service.get_info())
#
# print(order_service.order_id)
# print(order_service.get_info())


"""=========== 使用成员时不需要写前缀的导入方式，因为是直接以成员为单位导入 ==========="""

"""
方式一：我们可以从模块里只导入想使用的成员，而不是把整个模块全部导入，这种情况下就必须得用 from import、不能用 import

有时可能会用到，这里体现了 as 的第二个用途：不同模块里的成员命名冲突时，可以用 as 给成员取别名来避免冲突
"""
# from service.user_service import user_name, get_info as get_user_info
# from service.order_service import get_info as get_order_info
#
# print(user_name)
# print(get_user_info())
#
# print(get_order_info())

# 方式二：一次性从某个模块里导入所有公开成员，这种情况下就必须得用 from import、不能用 import
#
# 不推荐，因为这种方式很容易出现“后导入模块里的成员会覆盖先导入模块里的同名成员”这种现象，但是编译又不报错，只有运行时才会发现 bug
# from service.user_service import *
# from service.order_service import *
#
# print(user_name)
# print(get_info())
#
# print(order_id)
# print(get_info())
