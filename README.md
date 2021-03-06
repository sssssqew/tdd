# selenium 을 AWS와 같은 CLI 환경에서 실행하는 경우 아래와 같은 설정이 필요함
# 하지만 로컬 PC에서도 --liveserver 옵션을 이용해서 원격으로 서버 FT 실행가능함     
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


# 자동 배포후 스테이징 서버와 운영서버 모두 gunicorn을 재실행해야 한다.
# sudo systemctl start gunicorn-sylee.co.kr.service
# sudo systemctl start gunicorn-live.sylee.co.kr.service
```

# 페브릭 자동화 스크립트가 제대로 실행되지 않는 경우 

SSH Key 생성 및 서버에 등록해 줘야 한다. 

```
ssh-keygen -t rsa
ls -al ~/.ssh/

chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_rsa
chmod 644 ~/.ssh/id_rsa.pub  
chmod 644 ~/.ssh/authorized_keys
chmod 644 ~/.ssh/known_hosts

# 로컬 pc의 id_rsa.pub 파일을 리모트 서버의 $HOME/.ssh/authorized_keys 파일에 쓰기 
# 로컬 pc에서  ssh -v sylee.co.kr 등으로 서버(AWS도 포함)에 원격접속이 가능함
# 운영서버와 스테이징 서버 모두 하나의 서버 안에서 실행할 수 있다 
```

https://opentutorials.org/module/432/3742

# socket.gaierror: [Errno -2] Name or service not known 에러 발생시 
```
vim /etc/hosts 파일의 127.0.0.1 localhost 주석 해제하기 
```

# session not created exception 에러 발생시 
```
chromedriver 버전이 해당 크롬 브라우저 버전을 지원하지 않아서 생기는 문제
chromedriver 버전을 브라우저 버전에 호환되도록 다시 다운로드하기 
```

# 로그아웃 기능 구현시 'bool' object is not callable 에러 발생시 

```
1. 아래 파일 수정하기 
tdd/virtualenv/lib/python3.5/site-packages/django/contrib/auth/__init__.py
2. /is_authenticated()
3. is_authenticated() 메소드를 is_authenticated 속성으로 수정하기 
4. 로컬pc뿐만 아니라 스테이징 서버와 운영서버의 동일한 코드 부분도 모두 수정
5. 서버 gunicorn restart 및 nginx restart
```
