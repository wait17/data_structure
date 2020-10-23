"""
查看: settings -> live Templates -> user
文件头(快捷键 as)
Author:Ms.Ren
"""

# print("hello world")

# 第一种参数说明:
def hanshu(x,y):
    """
    参数说明(函数说明) (快捷键 函数下 -> """""" -> 回车)
    :param x: 第一个加数(待加的第一个加数)
    :type x: 整数(int)
    :param y: 第二个加数(待加的第二个加数)
    :type y: int
    :return: 返回两数之和
    :rtype: int
    """
    return x + y

# 第二种参数说明: 类型注解
def add(x: int,y: int) -> int:
    """
    :param x: 待加的第一个加数
    :param y: 待加的第二个加数
    :return: 返回两数之和
    """
    return x + y

# 设置方法: ----------------------------------------------------------
# 1. File -> Settings -> Editor -> Live Templates
# 2. + -> Live Templates 设置以下参数
# {Abbreviation:你想使用的快捷键(ds)
# Description:快捷键描述(文档注释)
# Applicable:可应用的语言范围(python)
# Template text :{
# """
# :Author:  Mr.Zhang                                ##### 格式 :内容名: 内容
# :Create:  $DATE$ $TIME$                           ##### 日期 + 时间
# :Github:  https://github.com/WeaponMaster
# Copyright (c) 2020, Mr.Zhang Group All Rights Reserved.
# """}
# }
# ----------------------------------------------------------
# File -> Settings -> Editor -> General -> SmartKeys
# 勾选
# Insert documentation comment stub
# Insert type placeholders in the documentation comment stub option
