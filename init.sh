# clone odoo
git clone -b 12.0 --depth=1 https://github.com/odoo/odoo.git web

git submodule add ./web
rm ./web/requirements.txt
# rm ./web/Dockerfile

cp Dockerfile ./web
cp requirements.txt ./web
mkdir web-data
chmod 777 ./web-data

mkdir addons
chmod 777 ./addons