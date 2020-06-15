#! usr/bin/env python3
# -*- coding:utf-8 _*-
import os, sys
sys.path.append (os.getcwd()+"/acme_package")
from acme_package.Acme_Deploy_Domain import *
# from Acme_Deploy_Domain import Acme_Deploy_Domain
import subprocess


carte = '''
Acme ：
        1.安装Acme.sh
        2.配置域名
        3.更新域名
        4.更新Acme.sh
        0.退出

您选择数字是：'''

snap = ""
success = ""
domain = ""
dns_str = "--dns --yes-I-know-dns-manual-mode-enough-go-ahead-please"
acme = "/root/.acme.sh/acme.sh"
dns_log = '/root/.acme.sh/dns.log'

class Acme():

    def __init__(self):
        while True:
            try:
                number = int(input(carte))
                exit()if number == 0 else \
                    self.install_acme() if number == 1 else \
                        self.deploy_domain() if number == 2 else \
                            self.update_domain() if number == 3 else \
                                self.update_acme() if number == 4 else \
                                    print("你输入有误，请重新输入")
            except Exception:
                exit("失败，异常退出")
            else:
                exit("{} {}".format(snap, success))

    def install_acme(self):
        if not os.path.exists("/root/.acme.sh"):
            global snap, success
            while snap == "":
                subprocess.check_call("curl https://get.acme.sh | sh", shell=True)
                if subprocess.getstatusoutput("{} -v".format(acme))[0] == 0:
                    subprocess.check_call("alias acme.sh={}".format(acme), shell=True)
                    subprocess.check_call("echo 'alias acme.sh={}' >>/etc/profile".format(acme), shell=True)
                    snap = "Acme.sh"
                    success = "Install Success"
        else:
            exit('已经安装了Acme.sh')

    def deploy_domain(self):
        Acme_Deploy_Domain()

    def update_domain(self):
        global snap, success
        if subprocess.check_call("{0} --cron --home /root/.acme.sh".format(acme), shell=True) == 0:
            snap = "Domain"
            success = "Update Success"

    def update_acme(self):
        global snap, success
        if subprocess.getstatusoutput("{} --upgrade".format(acme))[0] == 0:
            snap = "Acme.sh"
            success = "Update Success"

