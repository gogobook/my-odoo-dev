# 本分支用以建立m-odoo，及其所需的odoo 開發環境。
odoo/addons 只留下base_import, base_import_module, base_setup, base_sparse_field, bus, http_routing,
mail, resource, web, web_tour 其餘可刪除。
做法改為先將這幾個檔案cp 到某個地方，然後將整個addons 砍掉，最後將某個地方改名為addons

# web 資料夾內缺一Dockerfile, 原本的requirements.txt 也得修改。
在原本的另一個repository 中有，但是刪了。還好github 可以救回來，謝天謝地，弄那兩個檔案也是很花時間的。  
**那兩個檔案非常重要！**  
**werkzeug版本是0.16.1,python是3.8**   
# 直接修改odoo.conf 即可。

# 另，要使用git submodule add ./web

## 直接執行 init.sh

## web-data 應該可以被放到redis 中，特別是session 的部分。不過這部分應該也還好。

## Deploying with Gunicorn
**不需要gevent參數**
~~加上`gevent` 即可，其他都不用了。~~
```py
# For gunicorn additional globals need to be defined in the Gunicorn section.
# Then the following command should run:
#   $ gunicorn odoo:service.wsgi_server.application -c openerp-wsgi.py
```
這個`openerp-wsgi.py` 在odoo 中有個說明有提到這隻程式，但實際上就是`odoo`
ex:
```py
# openerp-wsgi.py
import openerp # 這裡其實是odoo
conf = openerp.tools.config
conf['addons_path'] = '/home/openerp/addons/trunk,/home/openerp/web/trunk/addons'
```
The above three lines first import the `openerp` library (i.e. the one containing the OpenERP server implementation). The second one is really to shorten repeated usage of the same variable. The third one sets a parameter, in this case the equivalent of the `--addons-path` command-line option.

# Deploying Odoo
https://www.odoo.com/documentation/13.0/setup/deploy.html

大概只有nginx 的設定那個部分比較有用一些其他沒什麼用。

可能要寫一個批次檔，以處理static 不然有點不好。

## Odoo as a WSGI Application

It is also possible to mount Odoo as a standard WSGI application. Odoo provides the base for a WSGI launcher script as `odoo-wsgi.example.py`. That script should be customized (possibly after copying it from the setup directory) to correctly set the configuration directly in `odoo.tools.config` rather than through the command-line or a configuration file.

However the WSGI server will only expose the main HTTP endpoint for the web client, website and webservice API. Because Odoo does not control the creation of workers anymore it can not setup cron or livechat workers

### Cron Workers
To run cron jobs for an Odoo deployment as a WSGI application requires

- A classical Odoo (run via `odoo-bin`)
- Connected to the database in which cron jobs have to be run (via `odoo-bin -d`)
- Which should not be exposed to the network. To ensure cron runners are not network-accessible, it is possible to disable the built-in HTTP server entirely with `odoo-bin --no-http` or setting `http_enable = False` in the configuration file

### LiveChat

The second problematic subsystem for WSGI deployments is the LiveChat: where most HTTP connections are relatively short and quickly free up their worker process for the next request, LiveChat require a long-lived connection for each client in order to implement near-real-time notifications.

This is in conflict with the process-based worker model, as it will tie up worker processes and prevent new users from accessing the system. However, those long-lived connections do very little and mostly stay parked waiting for notifications.

The solutions to support livechat/motifications in a WSGI application are:

- Deploy a threaded version of Odoo (instread of a process-based preforking one) and redirect only requests to URLs starting with `/longpolling`/ to that Odoo, this is the simplest and the longpolling URL can double up as the cron instance.
- Deploy an evented Odoo via odoo-gevent and proxy requests starting with `/longpolling/` to the `longpolling port`.