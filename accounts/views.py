from django.shortcuts import redirect 
from django.core.mail import send_mail
from accounts.models import Token
from django.core.urlresolvers import reverse
from django.contrib import auth, messages

def send_login_email(request):
	email = request.POST['email']
	token = Token.objects.create(email=email)
	url = request.build_absolute_uri(
		reverse('login') + '?token=' + str(token.uid)
	)
	message_body = 'Use this link to log in:\n\n' + url
	# let's think about send_mail to external API call
	print(type(send_mail))
	send_mail(
		'Your login link for Superlists',
		message_body,
		'noreply@superlists',
		[email],
	)
	messages.success(
		request,
		"Check your email, we've sent you a link you can use to log in."
	)
	return redirect('/') 

def login(request):
	user = auth.authenticate(uid=request.GET.get('token'))
	if user:
		# add user to request when redirecting
		auth.login(request, user)
	return redirect('/')


