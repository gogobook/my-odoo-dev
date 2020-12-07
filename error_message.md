目前有一個Session expired，這是由另一個odoo 造成的

## 目前website 的login 觸發了以下這個錯誤，待處理。
目前處理方式為直接註解掉，待後續解決。  
Your Odoo session expired. The current page is about to be refreshed.
```log
  File "/usr/src/app/addons/mail/controllers/home.py", line 40, in _login_redirect
    _admin_password_warn(uid)
  File "/usr/src/app/addons/mail/controllers/home.py", line 18, in _admin_password_warn
    if ipaddress.ip_address(request.httprequest.remote_addr).is_private:
  File "/usr/local/lib/python3.8/ipaddress.py", line 53, in ip_address
    raise ValueError('%r does not appear to be an IPv4 or IPv6 address' %
Exception
```

```sh
(odoo) lee@lee-MS-7995:.../odoo/odoo13$ docker-compose logs web
Attaching to odoo13_web_1
web_1  | 2020-01-08 11:02:40,640 6 INFO ? odoo: Odoo version 13.0 
web_1  | 2020-01-08 11:02:40,640 6 INFO ? odoo: Using configuration file at /etc/odoo/odoo.conf 
web_1  | 2020-01-08 11:02:40,641 6 INFO ? odoo: addons paths: ['/usr/src/app/odoo/addons', '/var/lib/odoo/addons/13.0', '/mnt/extra-addons'] 
web_1  | 2020-01-08 11:02:40,641 6 INFO ? odoo: database: default@default:default 
web_1  | 2020-01-08 11:02:40,641 6 CRITICAL ? odoo.modules.module: Couldn't load module web 
web_1  | 2020-01-08 11:02:40,641 6 CRITICAL ? odoo.modules.module: No module named 'odoo.addons.web' 
web_1  | 2020-01-08 11:02:40,641 6 ERROR ? odoo.service.server: Failed to load server-wide module `web`.
web_1  | The `web` module is provided by the addons found in the `openerp-web` project.
web_1  | Maybe you forgot to add those addons in your addons_path configuration. 
web_1  | Traceback (most recent call last):
web_1  |   File "/usr/src/app/odoo/service/server.py", line 1127, in load_server_wide_modules
web_1  |     odoo.modules.module.load_openerp_module(m)
web_1  |   File "/usr/src/app/odoo/modules/module.py", line 365, in load_openerp_module
web_1  |     __import__('odoo.addons.' + module_name)
web_1  | ModuleNotFoundError: No module named 'odoo.addons.web'
web_1  | 2020-01-08 11:02:40,727 6 INFO ? odoo.addons.base.models.ir_actions_report: Will use the Wkhtmltopdf binary at /usr/local/bin/wkhtmltopdf 
web_1  | 2020-01-08 11:02:40,833 6 INFO ? odoo.service.server: HTTP service (werkzeug) running on 9c9f56591d05:8069 
web_1  | 2020-01-08 11:04:58,635 6 INFO ? odoo.http: HTTP Configuring static files 
web_1  | 2020-01-08 11:04:58,664 6 INFO ? odoo.http: Generating nondb routing 
web_1  | 2020-01-08 11:04:58,666 6 INFO ? werkzeug: 172.21.0.1 - - [08/Jan/2020 11:04:58] "GET / HTTP/1.1" 404 - 1 0.024 0.006
web_1  | 2020-01-08 11:08:35,023 6 INFO ? werkzeug: 172.21.0.1 - - [08/Jan/2020 11:08:35] "GET / HTTP/1.1" 404 - 1 0.001 0.003
```
```sh
(odoo) lee@lee-MS-7995:.../odoo/odoo13$ docker-compose logs web
Attaching to odoo13_web_1
web_1  | 2020-01-08 11:11:52,773 6 INFO ? odoo: Odoo version 13.0 
web_1  | 2020-01-08 11:11:52,773 6 INFO ? odoo: Using configuration file at /etc/odoo/odoo.conf 
web_1  | 2020-01-08 11:11:52,774 6 INFO ? odoo: addons paths: ['/usr/src/app/odoo/addons', '/var/lib/odoo/addons/13.0', '/mnt/extra-addons'] 
web_1  | 2020-01-08 11:11:52,774 6 INFO ? odoo: database: default@default:default 
web_1  | 2020-01-08 11:11:52,857 6 INFO ? odoo.addons.base.models.ir_actions_report: Will use the Wkhtmltopdf binary at /usr/local/bin/wkhtmltopdf 
web_1  | 2020-01-08 11:11:53,025 6 INFO ? odoo.service.server: HTTP service (werkzeug) running on 504e7d2b8caf:8069 
web_1  | 2020-01-08 11:12:06,862 6 INFO ? odoo.http: HTTP Configuring static files 
web_1  | 2020-01-08 11:12:06,879 6 INFO ? odoo.http: Generating nondb routing 
web_1  | 2020-01-08 11:12:06,893 6 INFO ? werkzeug: 172.22.0.1 - - [08/Jan/2020 11:12:06] "GET / HTTP/1.1" 303 - 1 0.005 0.024
web_1  | 2020-01-08 11:12:06,919 6 INFO ? werkzeug: 172.22.0.1 - - [08/Jan/2020 11:12:06] "GET /web HTTP/1.1" 303 - 2 0.004 0.005
web_1  | 2020-01-08 11:12:07,108 6 INFO ? werkzeug: 172.22.0.1 - - [08/Jan/2020 11:12:07] "GET /web/database/selector HTTP/1.1" 200 - 2 0.005 0.167
web_1  | 2020-01-08 11:12:07,195 6 INFO ? werkzeug: 172.22.0.1 - - [08/Jan/2020 11:12:07] "GET /web/static/src/img/logo2.png HTTP/1.1" 200 - - - -
web_1  | 2020-01-08 11:12:07,195 6 INFO ? werkzeug: 172.22.0.1 - - [08/Jan/2020 11:12:07] "GET /web/static/lib/fontawesome/css/font-awesome.css HTTP/1.1" 200 - - - -
web_1  | 2020-01-08 11:12:07,196 6 INFO ? werkzeug: 172.22.0.1 - - [08/Jan/2020 11:12:07] "GET /web/static/lib/bootstrap/js/index.js HTTP/1.1" 200 - - - -
web_1  | 2020-01-08 11:12:07,196 6 INFO ? werkzeug: 172.22.0.1 - - [08/Jan/2020 11:12:07] "GET /web/static/lib/popper/popper.js HTTP/1.1" 200 - - - -
web_1  | 2020-01-08 11:12:07,196 6 INFO ? werkzeug: 172.22.0.1 - - [08/Jan/2020 11:12:07] "GET /web/static/lib/bootstrap/css/bootstrap.css HTTP/1.1" 200 - - - -
web_1  | 2020-01-08 11:12:07,202 6 INFO ? werkzeug: 172.22.0.1 - - [08/Jan/2020 11:12:07] "GET /web/static/lib/jquery/jquery.js HTTP/1.1" 200 - - - -
web_1  | 2020-01-08 11:12:07,210 6 INFO ? werkzeug: 172.22.0.1 - - [08/Jan/2020 11:12:07] "GET /web/static/lib/bootstrap/js/util.js HTTP/1.1" 200 - - - -
web_1  | 2020-01-08 11:12:07,214 6 INFO ? werkzeug: 172.22.0.1 - - [08/Jan/2020 11:12:07] "GET /web/static/lib/bootstrap/js/alert.js HTTP/1.1" 200 - - - -
web_1  | 2020-01-08 11:12:07,214 6 INFO ? werkzeug: 172.22.0.1 - - [08/Jan/2020 11:12:07] "GET /web/static/lib/bootstrap/js/button.js HTTP/1.1" 200 - - - -
web_1  | 2020-01-08 11:12:07,218 6 INFO ? werkzeug: 172.22.0.1 - - [08/Jan/2020 11:12:07] "GET /web/static/lib/bootstrap/js/carousel.js HTTP/1.1" 200 - - - -
web_1  | 2020-01-08 11:12:07,219 6 INFO ? werkzeug: 172.22.0.1 - - [08/Jan/2020 11:12:07] "GET /web/static/lib/bootstrap/js/collapse.js HTTP/1.1" 200 - - - -
web_1  | 2020-01-08 11:12:07,224 6 INFO ? werkzeug: 172.22.0.1 - - [08/Jan/2020 11:12:07] "GET /web/static/lib/bootstrap/js/dropdown.js HTTP/1.1" 200 - - - -
web_1  | 2020-01-08 11:12:07,226 6 INFO ? werkzeug: 172.22.0.1 - - [08/Jan/2020 11:12:07] "GET /web/static/lib/bootstrap/js/modal.js HTTP/1.1" 200 - - - -
web_1  | 2020-01-08 11:12:07,234 6 INFO ? werkzeug: 172.22.0.1 - - [08/Jan/2020 11:12:07] "GET /web/static/lib/bootstrap/js/tooltip.js HTTP/1.1" 200 - - - -
web_1  | 2020-01-08 11:12:07,239 6 INFO ? werkzeug: 172.22.0.1 - - [08/Jan/2020 11:12:07] "GET /web/static/lib/bootstrap/js/scrollspy.js HTTP/1.1" 200 - - - -
web_1  | 2020-01-08 11:12:07,240 6 INFO ? werkzeug: 172.22.0.1 - - [08/Jan/2020 11:12:07] "GET /web/static/lib/bootstrap/js/popover.js HTTP/1.1" 200 - - - -
web_1  | 2020-01-08 11:12:07,241 6 INFO ? werkzeug: 172.22.0.1 - - [08/Jan/2020 11:12:07] "GET /web/static/lib/bootstrap/js/tab.js HTTP/1.1" 200 - - - -
web_1  | 2020-01-08 11:12:07,319 6 INFO ? werkzeug: 172.22.0.1 - - [08/Jan/2020 11:12:07] "GET /web/static/lib/fontawesome/fonts/fontawesome-webfont.woff2?v=4.7.0 HTTP/1.1" 200 - - - -
```