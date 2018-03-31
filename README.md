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

# 우분투 16.04 이후 버전부터 upstart -> systemd 로 변경하기 

create a gunicorn.service file in /etc/systemd/system/
ex) /etc/systemd/system/gunicorn-sylee.co.kr.service

```
# Gunicorn Site systemd service file

[Unit]
Description=Gunicorn server for sylee.co.kr
After=network.target
After=syslog.target

[Service]
User=sylee
WorkingDirectory=/home/sylee/sites/sylee.co.kr
ExecStart=/home/sylee/sites/sylee.co.kr/virtualenv/bin/gunicorn --chdir /home/sylee/sites/sylee.co.kr/source superlists.wsgi:application --bind unix:/tmp/sylee.co.kr.socket
Restart=on-failure
RuntimeDirectory=gunicorn-stagingd
RuntimeDirectoryMode=755

# sudo systemctl start gunicorn-sylee.co.kr.service
```
