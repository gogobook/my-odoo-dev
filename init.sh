# clone odoo
git clone -b master --depth=1 https://github.com/odoo/odoo.git web

git submodule add ./web
rm ./web/requirements.txt
rm ./web/odoo/addons/base/__manifest__.py
rm ./web/odoo/addons/base/data/ir_module_module.xml
mkdir ./web/addons2
cp -r ./web/addons/base_import ./web/addons2/
cp -r ./web/addons/base_import_module ./web/addons2/
cp -r ./web/addons/base_setup ./web/addons2/
cp -r ./web/addons/base_sparse_field ./web/addons2/
cp -r ./web/addons/bus ./web/addons2/
cp -r ./web/addons/http_routing ./web/addons2/
cp -r ./web/addons/mail ./web/addons2/
cp -r ./web/addons/resource ./web/addons2/
cp -r ./web/addons/web ./web/addons2/
cp -r ./web/addons/web_tour ./web/addons2/
rm -r ./web/addons
mv ./web/addons2/ ./web/addons
cp manifest_for_m_odoo.py ./web/odoo/addons/base/__manifest__.py
cp Dockerfile ./web
cp requirements.txt ./web


mkdir web-data
chmod 777 ./web-data

touch .env

ADDONS_PATH="addons"
mkdir $ADDONS_PATH
chmod 777 ./$ADDONS_PATH
cd $ADDONS_PATH
git init
cd ..
git submodule add ./$ADDONS_PATH