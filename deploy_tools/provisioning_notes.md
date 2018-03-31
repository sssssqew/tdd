신규 사이트 프로비저닝 
===========================

## 필요 패키지 

* nginx 
* Python 3
* Git
* pip3
* virtualenv 

Ubuntu에서 실행 방법 예:

	sudo apt-get install nginx git python3 python3-pip
	sudo pip3 install virtualenv 

## Nginx 가상 호스트 설정 

* nginx.template.conf 참고 
* SITENAME 부분을 수정하기  

## Systemd Job

* gunicorn-systemd.template.service 참고 
* SITENAME 부분을 수정하기 

## 폴더 구조 
사용자 계정의 홈 폴더가 /home/sylee 이라고 가정 

/home/sylee/sites/SITENAME/ 아래 

* database
* source 
* static 
* virtualenv 


