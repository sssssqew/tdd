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
gunicorn-SITENAME-staging.example.com.service

```
# Gunicorn Site systemd service file

[Unit]
Description=Gunicorn server for SITENAME-staging.example.com
After=network.target
After=syslog.target

Environment=sitedir=/Development/sites/SITENAME-staging.example.com
ExecStart=$(sitedir)/virtualenv/bin/gunicorn --chdir $(sitedir)/source workouts.wsgi:application --bind unix:/tmp/SITENAME-staging.example.com.socket
Restart=on-failure
RuntimeDirectory=gunicorn-stagingd
RuntimeDirectoryMode=755


#sudo systemctl start gunicorn-SITENAME-staging.example.com.service
```
