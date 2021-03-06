*APP*

Append local domain to /etc/hots
```shell script
echo '127.0.0.1 localhost.dev' | sudo tee -a  /private/etc/hosts  # /etc/hosts for linux
```

Note: `dcp = docker-compose`

### Migration:

Create migration
```shell script
dcp run --rm app db migrate -m "Add new column"
sudo chmod -R 777 migrations  # only for linux
```
Run migration
```shell script
dcp run --rm app db upgrade heads
```

#### Starting
Run application
```shell script
dcp up app
```

### Other

Promote user as admin
```shell script
dcp run --rm app roles add hyzyla@gmail.com superuser
```

Update requirements.txt
```shell script
# install pip-tools
python3 -m pip install --user pip-tools
# add new requirement to requirements.in
echo 'django==2.0'>> filename
# Update requirements.txt via pip-compile

pip-compile requirements/base.in -o requirements/base.txt
```

# FRONTNED

```shell script
cd web
npm start
```

# Deploy
```shell script
git push dokku master  # for backend
cd web && git push dokku master # for frontend
```
