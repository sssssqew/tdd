# selenium 을 AWS와 같은 CLI 환경에서 실행하는 경우 아래와 같은 설정이 필요함     
1. [Install google chrome]
```
sudo apt-get update
sudo apt-get install google-chrome-stable
```

2. [Install chrome-driver]
```
wget http://chromedriver.storage.googleapis.com/2.37/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
```

3. [Run following commands to start selenium web server]
(커맨드 창을 새로 띄울때마다 아래 명령어를 실행해 줘야함)

```
nohup sudo Xvfb :10 -ac
export DISPLAY=:10
java -jar vendor/se/selenium-server-standalone/bin/selenium-server-standalone.jar -Dwebdriver.chrome.bin="/usr/bin/google-chrome" -Dwebdriver.chrome.driver="vendor/bin/chromedriver"
```

# upstart -> systemd

create a gunicorn.service file in /etc/systemd/system/

```
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=nero
Group=www-data WorkingDirectory=/path/to/webapp ExecStart=/path/to/webapp/virtual_env/bin/gunicorn --workers 3 --bind unix:/path/to/webapp/project.sock project.wsgi:application

[Install]
WantedBy=multi-user.target
```
started using sudo systemctl start gunicorn
