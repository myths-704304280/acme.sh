#! usr/bin/env python3
# -*- coding:utf-8 _*-
class variable():
    def acme_var(self,
                 domain=None,
                 acme="/root/.acme.sh/acme.sh",
                 nginx="/etc/nginx",
                 nginx_certs="/etc/nginx/certs",
                 nginx_reload="/etc/init.d/nginx force-reload"):
        dict = {
            'domain': domain,
            'acme': acme,
            'nginx': nginx,
            'nginx_certs': nginx_certs,
            'nginx_reload': nginx_reload
        }
        return dict

