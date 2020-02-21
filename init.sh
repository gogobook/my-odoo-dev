# clone odoo
git clone -b 13.0 --depth=1 https://github.com/odoo/odoo.git web

git submodule add ./web
rm ./web/requirements.txt
rm ./web/Dockerfile
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