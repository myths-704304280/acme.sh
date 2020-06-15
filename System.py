#! usr/bin/env python3
# -*- coding:utf-8 _*-
import platform

class System():
    name = "系统无法识别"
    system = ["el7", "el6", "Ubuntu", "debian"]
    def __init__(self):
        for i in self.system:
            if platform.platform().find("{}".format(i)) != -1:
                self.name = i

# *args 不同的包，可以对应相应的系统进行安装，只能输入2个包的名称,第一个参数是centos安装的包，第二个是ubantu、debian安装的包，同样的包只需要输入一个名称即可
def install(*args):
    software = list(args)

    if System().name == "el7" or System().name == "el6":
        install = "yum install {} -y".format(software[0])
    else:
        install = "sudo apt-get install {} -y".format(software[-1])

    return install

def start(name, command):
    wait = "sudo service {1} {0}".format(command, name) if System().name == "el6" else "sudo systemctl {1} {0} ".format(name, command)
    return wait

def init_start(name, command):
    wait = "sudo /etc/init.d/{0} {1}".format(name, command)
    return wait