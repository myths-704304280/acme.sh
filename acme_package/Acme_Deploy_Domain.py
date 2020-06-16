#! usr/bin/env python3
# -*- coding:utf-8 _*-
import os, sys
# sys.path.append(os.path.dirname(os.getcwd()+"/acme_package"))
# from acme_package.Acme import *
from Acme import *
from System import *
import subprocess


carte = '''
Acme ：
        1.DNS 手工模式
        2.DNS API模式
        3.DNS 别名模式
        
        0.退出

您选择数字是：'''
certs = "/etc/nginx/certs"


class Acme_Deploy_Domain(Acme):

    def __init__(self):
        global domain
        domain = input("请输入你要注册证书的域名: ")
        while True:
            try:
                number = int(input(carte))
                exit()if number == 0 else \
                    self.dns_manual_mode() if number == 1 else \
                        self.dns_api_mode() if number == 2 else \
                            self.dns_alias_mode() if number == 3 else \
                                    print("你输入有误，请重新输入")
            except Exception:
                exit("失败，异常退出")

    def dns_manual_mode(self):
        test_log = '/root/.acme.sh/set_up.log'
        issue = "{0} --issue -d {1} -d *.{1} {2}".format(acme, domain, dns_str)
        renew = "{0} --renew -d {1} -d *.{1} {2}".format(acme, domain, dns_str)
        if subprocess.getstatusoutput("which dig")[0] != 0:
            subprocess.call(install("bind-utils", "dnsutils"), shell=True)

        subprocess.call("touch {0} {1}".format(dns_log, test_log), shell=True)

        snap = ""
        while snap == "":
            count, dns = 0, ""

            subprocess.call("{}".format(issue + "| grep -E 'value|Domain' | awk -F {0} '{1}' > {2}".format('"\'"', "{print $2}", dns_log)), shell=True)

            for line in open(dns_log, 'r'):
                dns += line
                count += 1

            if count == 1:
                self.acme_install_cert()
                exit("此域名不需要配置")
            elif count == 4:
                input("请添加 DNS 解析: \n {} \n 添加完成请安任意键继续".format(dns))
            else:
                exit("域名证书配置失败")

            subprocess.check_call("dig -t txt _acme-challenge.{0} | grep {0} | awk -F {1} {2} > {3}".format(domain, "'\"'", "'{print $2}'", test_log), shell=True)
            for i in open(dns_log, 'r').readlines():
                for y in open(test_log, 'r').readlines():
                    if i in y:
                        count += 1
            print(count)
            if count == 6:
                subprocess.check_call(renew, shell=True)
                self.acme_install_cert()

    def dns_api_mode(self):
        dict, firm = [], ''
        print("腾讯/DNSPod：DP_Id|DP_key \n 阿里云: Ali_Secret|Ali_Key \n CloudFlare: CF_Email|CF_Key \n 其他 \n 例如 \nDP_Id='123' \nDP_Key='aaa'  \n" )
        print("请输入API值 输入完毕，请输入ok")
        while True:
            api = input("export ")

            if api in "ok":
                break
            dict.append(api)
            # 获取“_”前的字符
            firm = dict[0][0:dict[0].index("_")]
        print(dict)
        for export in dict:
            print(export)
            subprocess.check_call("export {}".format(export), shell=True)
            # subprocess.check_call("echo SAVED_{} >> /root/.acme.sh/account.conf".format(export), shell=True)

        #firm.lower()把大写转化为小写字母
        subprocess.check_call("{0} --issue -d {1} -d *.{1} --dns dns_{2}".format(acme, domain, firm.lower()), shell=True)
        self.acme_install_cert()

    def dns_alias_mode(self):
        api_domian = input("输入在本机拥有AIP验证的域名: ")
        firm = input("例如：\n腾讯/DNSPod   'DP' \n阿里云   'Ali' \nCloudFlare   'CF' \n请输入拥有AIP验证域名的厂商: " )
        input("请在这个域名：{0}，\n添加DNS CNAME记录值: _acme-challenge.{0}     CNAME    _acme-challenge.{1} \n添加完成请按任意键继续 ".format(domain, api_domian))
        subprocess.check_call("{0} --issue -d {1} -d *.{1} --challenge-alias {2} --dns dns_{3}".format(acme, domain, api_domian, firm.lower()), shell=True)
        self.acme_install_cert()


    def acme_install_cert(self,certs=certs):
        if os.path.isdir(certs) == False:
            os.mkdir(certs)
        subprocess.check_call("{0} --install-cert -d {1} -d *.{1} "
                              "--key-file {3}/{1}.key "
                              "--fullchain-file {3}/{1}.fullchain.crt "
                              "--reloadcmd \"{2}\" ".format(acme, domain, start("nginx", "force-reload"), certs), shell=True)
        exit("deploy \"{}\" success".format(domain))

