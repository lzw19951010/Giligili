from django.contrib import auth
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.db import models
import os 

def login(request, error_msg=""):
	error_msg = ''
	if request.user.is_authenticated():
		return HttpResponseRedirect("/home/")
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				auth.login(request, user)
				return HttpResponseRedirect("/home/")
			else:
				error_msg = '该用户无法正常使用'
				return render(request, "login.html", {'username': username, 'context': error_msg})
		else:
			error_msg = '用户名或密码错误'
			return render(request, "login.html", {'username': username, 'context': error_msg})
	else:
		return render(request, "login.html")
		
		
def register(request, error_msg=""):
	if request.user.is_authenticated():
		return HttpResponseRedirect("/home/")
	if request.method == 'POST':
		input_is_valid = False
		username = request.POST['username'] if request.POST['username'] else ""
		password1 = request.POST['password1'] if request.POST['password1'] else ""
		password2 = request.POST['password2'] if request.POST['password2'] else ""
		nickname = request.POST['nickname'] if request.POST['nickname'] else ""
		email = request.POST['email'] if request.POST['email'] else ""
		description = request.POST['description'] if request.POST['description'] else ""
		print(nickname, description)
		error_msg = "错误"
		if not username:
			error_msg = "请输入用户名"
		elif not (password1 and password2):
			error_msg = "请输入密码"
		elif not nickname:
			error_msg = "请输入昵称"
		elif not email:
			error_msg = "请输入邮箱"
		elif not description:
			error_msg = "请输入个人描述"
		elif password1 != password2:
			error_msg = "两次密码不一致"
		elif len(password1) < 6:
			error_msg = "密码长度小于6位"
		elif User.objects.filter(username=username):
			error_msg = "用户名已经存在"
			username = ""
		elif User.objects.filter(email=email):
			error_msg = "邮箱已经注册"
			email = ""
		#elif User.objects.filter(UNickname=nickname):
		#	error_msg = "昵称已经存在"
		#	email = ""
		else:
			input_is_valid = True
			user = User.objects.create_user(username = username, password = password1, email = email)
			user.save()
			thisProfile = UserExtraProfile(user = user, UNickName = nickname, UDescription = description)
			thisProfile.save()
			print('saved')
			return HttpResponseRedirect("/")
		if not input_is_valid :
			return render(request, "register.html", {'error': error_msg, 'username': username, 'nickname': nickname, 'email': email, 'description': description})
	else:
		return render(request, "register.html")
		
def logout(request):
	auth.logout(request)
	return render(request, "logout.html")
	
class UserExtraProfile(models.Model):
	user = models.OneToOneField(User)
	UNickName = models.CharField(max_length=20)
	UDescription = models.CharField(max_length=50)
	
class Video(models.Model):
	VTitle = models.CharField(max_length=50)
	VUploader = models.ForeignKey(UserExtraProfile)
	
class Notification(models.Model):
	NContent = models.CharField(max_length=50)
	NUser = models.ForeignKey(UserExtraProfile)
