# WSGI Handler sample configuration file.
#
# Change the appropriate settings below, in order to provide the parameters
# that would normally be passed in the command-line.
# (at least conf['addons_path'])
#
# For generic wsgi handlers a global application is defined.
# For uwsgi this should work:
#   $ uwsgi_python --http :9090 --pythonpath . --wsgi-file openerp-wsgi.py
#
# For gunicorn additional globals need to be defined in the Gunicorn section.
# Then the following command should run:
#   $ gunicorn odoo:service.wsgi_server.application -c openerp-wsgi.py

import odoo

#----------------------------------------------------------
# Common
#----------------------------------------------------------
odoo.multi_process = True # Nah!

# Equivalent of --load command-line option
conf = odoo.tools.config
conf['addons_path'] = '/usr/src/app/odoo/addons,/usr/src/app/addons,/mnt/extra-addons'
odoo.conf.server_wide_modules = ['base', 'web']

# Path to the OpenERP Addons repository (comma-separated for
# multiple locations)
# 

conf['proxy_mode'] = True

# Optional database config if not using local socket
# conf['db_name'] = 'mycompany'
conf['db_host'] = 'db'
conf['db_user'] = 'odoo'
conf['db_port'] = 5432
conf['db_password'] = 'myodoo'

#----------------------------------------------------------
# Generic WSGI handlers application
#----------------------------------------------------------
application = odoo.service.wsgi_server.application

odoo.service.server.load_server_wide_modules()

#----------------------------------------------------------
# Gunicorn
#----------------------------------------------------------
# Standard OpenERP XML-RPC port is 8069
# bind = '0.0.0.0:8069'
bind = 'unix:/var/run/gunicorn/gunicorn.sock'
pidfile = '.gunicorn.pid'
workers = 4
timeout = 240
max_requests = 2000