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
#   $ gunicorn odoo:service.wsgi_server.application -c odoo-wsgi.py
```
在setup 資料夾中有一個`odoo-wsgi.example.py`，作為odoo-wsgi.py 的例子。
ex:
```py
# odoo-wsgi.py
import odoo # 這裡其實是odoo
conf = odoo.tools.config
conf['addons_path'] = '/home/odoo/addons/trunk,/home/odoo/web/trunk/addons'
```
The above three lines first import the `odoo` library (i.e. the one containing the odoo server implementation). The second one is really to shorten repeated usage of the same variable. The third one sets a parameter, in this case the equivalent of the `--addons-path` command-line option.

# Deploying Odoo
https://www.odoo.com/documentation/14.0/setup/deploy.html

大概只有nginx 的設定那個部分比較有用一些其他沒什麼用。

可能要寫一個批次檔，以處理static 不然有點不好。

# 測試

[odoo testing](https://www.odoo.com/documentation/14.0/reference/testing.html)
待實驗及實作

整合測試應該使用selenium 或許會更好一些。