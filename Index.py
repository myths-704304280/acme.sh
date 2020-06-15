#! usr/bin/env python3
# -*- coding:utf-8 _*-
from acme_package import *
hint = '''
请选择：
        1.Acme,检查、安装、更新
        0.退出

您选择数字是：'''

while True:
    number = input(hint)

    if number == "0":
        break

    Acme.Acme() if number == "1" else print("您输入有误,请重新输入")







