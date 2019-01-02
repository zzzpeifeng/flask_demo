
#from . 相当于导入users包
from . import users_blu


"""
    专门用户存放模块下所有的视图函数
"""


@users_blu.route("/users")
def users():
    return users