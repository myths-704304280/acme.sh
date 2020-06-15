#! usr/bin/env python2
# -*- coding:utf-8 _*-
import os, sys
# sys.path.append("{}/acme_package".format(os.getcwd()))
from System import *

class Install(System):

    compile_and_install = [
        "tar -zxvf Python-3.8.3.tgz",
        "Python-3.8.3/configure --prefix=/usr/local/python3 ",
        "make | make install",
        "ln -s /usr/local/python3/bin/python3 /usr/bin/python3",
        "make | make install",
        "ln -s /usr/local/python3/bin/python3 /usr/bin/python3",
        "which python3"
    ]

    apt_install = [
        "sudo apt-get update",
        "sudo apt-get install python3 -y",
        "sudo which python3"
    ]

    def __init__(self):

        # self.yum_install_python3() if self.name == "centos" else self.apt_install_python3()
        self.yum_install_python3() if System().name == "el7" or System().name == "el6" else self.apt_install_python3()

    def apt_install_python3(self):
        i = ""
        for i in self.apt_install:
            os.system(i)
        if os.system(i) == 0:
            print("python3 安装成功")

    def yum_install_python3(self):
        i = "mkdir -p /usr/local/python3"
        if os.system("wget https://www.python.org/ftp/python/3.8.3/Python-3.8.3.tgz") and os.system(i) == 0:
            for i in self.compile_and_install:
                os.system(i)
            if os.system(i) == 0:
                print("python3 安装成功")
        else:
            print("python3 下载失败")

if __name__ == '__main__':
    Install().__init__()