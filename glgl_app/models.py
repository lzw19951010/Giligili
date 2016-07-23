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
			return HttpResponseRedirect("/")
		if not input_is_valid :
			return render(request, "register.html", {'error': error_msg, 'username': username, 'nickname': nickname, 'email': email, 'description': description})
	else:
		return render(request, "register.html")

def profile(request, error_msg=''):
	if request.user.is_authenticated():
		if request.method == 'POST':
			username = request.POST['username']
			password1 = request.POST['password1'] if request.POST['password1'] else ""
			nickname = request.POST['nickname'] if request.POST['nickname'] else ""
			description = request.POST['description'] if request.POST['description'] else ""
			user = auth.authenticate(username=username, password=password1)
			if user is not None:
				if user.is_active:
					profile = user.userextraprofile
					profile.UNickName = nickname
					profile.UDescription = description
					profile.save()
					#更改个人信息
					return render(request, "home.html", {'context': '信息更改成功'})
				else:
					error_msg = '该用户无法正常使用'
					return render(request, "home.html", {'context': error_msg})
			else:
				error_msg = '密码错误'
				return render(request, "home.html", {'context': error_msg})
		else:
			return render(request, "home.html")
	else:
		error_msg = '请先登录'
		return render(request, "home.html", {'context': error_msg})

def setPassword(request, error_msg=""):
	if request.user.is_authenticated() :
		if request.method == 'POST':
			input_is_valid = False
			password = request.POST['password'] if request.POST['password'] else ""
			newpassword1 = request.POST['newpassword1'] if request.POST['newpassword1'] else ""
			newpassword2 = request.POST['newpassword2'] if request.POST['newpassword2'] else ""
			error_msg = "错误"
			if not password:
				error_msg = "请输入原密码"
			elif not newpassword1:
				error_msg = "请输入新密码"
			elif not newpassword2:
				error_msg = "请确认新密码"
			elif newpassword1 != newpassword2:
				error_msg = "两次密码不一致"
			elif len(newpassword1) < 6:
				error_msg = "密码长度小于6位"
			elif request.user.check_password(password)==False:
				error_msg = "密码错误"
			else:
				input_is_valid = True
				request.user.set_password(newpassword1)
				request.user.save()
				return HttpResponseRedirect("/setpassword-suc")
			if not input_is_valid :
				return render(request, "setpassword.html", {'error': error_msg})
		else:
			return render(request, "setpassword.html")
	else:
		error_msg = "请先登录"
		return render(request,"login.html",{'error': error_msg})

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

